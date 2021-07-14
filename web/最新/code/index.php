<?php

$today = date("F j, Y, g:i a"); 
echo $today;


?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index</title>
    <link rel="stylesheet" href="css/index.css">
    <link rel="stylesheet" href="css/header.css">
    <link rel="stylesheet" href="css/ress.css">
    <link rel="stylesheet" href="css/common.css">
    <link rel="stylesheet" href="css/vars.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Swiper/6.7.0/swiper-bundle.css" integrity="sha512-lfjMBfE41+3a9XCiuXCjaE4CkvpPOQ5P2qZSZclW9iHsMSvn50dh6ZuB5O8g7uDlCIKFKPqYo8JIka9Rh8HXow==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
    <header>
        <div class="header__imgBox">
            <div class="swiper-container">
                <div class="swiper-wrapper">
                    <div class="swiper-slide"><img src="img/AdobeStock_96604330.jpeg" alt=""></div>
                    <div class="swiper-slide"><img src="img/AdobeStock_44616117.jpeg" alt=""></div>
                    <div class="swiper-slide"><img src="img/AdobeStock_193895109.jpeg" alt=""></div>
                </div>
            </div>
            <h2><img src="img/index_main_img_text.svg" alt=""></h2>
        </div>
        <nav>
            <div class="nav">
                <div class="nav__bg"></div>
                <div class="nav__flex">
                    <div class="nav__flex__logo">
                        <h1><a href="#"><img src="img/logo.svg" alt=""></a></h1>
                    </div>
                    <div class="nav__flex__items">
                        <ul>
                            <li><a href="#">ホーム</a></li>
                            <li><a href="#">レース予想</a></li>
                            <li><a href="#">ランキング</a></li>
                            <li><a href="#">マイページ</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </nav>
    </header>
    <!-- レース情報 -->
    <div class="race">
        <h2>今週のレース</h2>
        <div class="race__box">
            <div class="race__box__main">
                <div class="race__box__main__title">
                    <h3>日本ダービー<span>GI</span></h3>
                    <p>東京競馬場 芝 2400m </p>
                    <p>5月30日 (日)</p>
                </div>
                <div class="race__box__main__table">
                    <table rules="all">
                        <tr>
                            <th>枠番</th>
                            <th>馬番</th>
                            <th>馬名</th>
                            <th>オッズ</th>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>4</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>4</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>5</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>5</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>6</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>6</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>7</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>7</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>8</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                        <tr>
                            <td>8</td>
                            <td>1</td>
                            <td>エフフォーリア</td>
                            <td>1.7</td>
                        </tr>
                    </table>
                </div>
                <div class="race__box__main__expected">
                    <p><a href="#">予想を見る</a></p>
                </div>
            </div>
            <div class="race__box__sub">
                <div class="race__box__sub__items">
                    <a href="#">
                        <h3>葵ステークス<span class="GroupRace">重賞</span></h3>
                        <p>中京競馬場 芝 1200m</p>
                        <p>5月29日 (土)</p>
                    </a>
                </div>
                <div class="race__box__sub__items">
                    <a href="#">
                        <h3>日本ダービー<span class="G1">GⅠ</span></h3>
                        <p>東京競馬場 芝 2400m </p>
                        <p>5月30日 (日)</p>
                    </a>
                </div>
                <div class="race__box__sub__items">
                    <a href="#">
                        <h3>目黒記念<span class="G2">GⅡ</span></h3>
                        <p>東京競馬場 芝 2500m </p>
                        <p>5月30日 (日)</p>
                    </a>
                </div>
            </div>
        </div>
    </div>
    <!-- レース情報 -->

    <div class="balance">
        <h2>残高確認</h2>
        <div class="balance__box">
            <div class="balance__box__content">
                <h3>現在の残高</h3>

            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Swiper/6.7.0/swiper-bundle.min.js" integrity="sha512-qqdD5ZLIGB5PCqCk1OD8nFBr/ngB5w+Uw35RE/Ivt5DK35xl1PFVkuOgAbqFpvtoxX6MpRGLmIqixzdhFOJhnA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="js/index.js"></script>
</body>

</html>