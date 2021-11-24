import sys, time, os
from os import system

# DSC Galatasaray | Python | Örnek Projeler

devam = " [ Devam etmek için Enter'a basınız... ]"

walking_frames = [
    [
        # ----------Frame I---------- #
        f"             `-:-`          ",
        f"            -ydddy.         ",
        f"            +ddddm/         ",
        f"            .ohhh+`         ",
        f"           `.:++.           ",
        f"         `:sdddds`          ",
        f"        `odoymmmd+`         ",
        f"        :do sdddshy+.`      ",
        f"        oy. ohyy-.:oy+`     ",
        f"        ``  sysho.          ",
        f"           .ys./ys.         ",
        f"          `yd/` /dh.        ",
        f"        `/yds`  `odh.       ",
        f"      .ohhs:     `yds       ",
        f"      ./:.        .so`      ",

    ],
    [
        # ---------Frame II---------- #
        f"              `.-.`         ",
        f"             .shddy-        ",
        f"             odmmmdy        ",
        f"             .shdhy-        ",
        f"             `:++-`         ",
        f"           `+hddd/          ",
        f"          `yhhddmy`         ",
        f"          :m+yddmds.`       ",
        f"          -dohmmd+yy+.      ",
        f"           +odmdds..-`      ",
        f"            `hmo+hy-        ",
        f"           `:hd-`ody`       ",
        f"       `/+oshy/  -dd-       ",
        f"       .sso/-`   :dh.       ",
        f"                 /s/        "

    ],
    [
        # --------Frame III---------- #
        f"               `..`         ",
        f"              /yhdh+`       ",
        f"             .hmmmmm-       ",
        f"             `+hddho`       ",
        f"              `:+:.         ",
        f"            `:yddy`         ",
        f"            /dmmmy`         ",
        f"            ydmddh.         ",
        f"            +ddmmds-        ",
        f"            `sdmdmdy`       ",
        f"             .hmyhd+        ",
        f"           ``.hd+/dm.       ",
        f"         /syyhy+`:hm-       ",
        f"         -//:.`  ody        ",
        f"                `oo`        "
    ],
    [
        # ---------Frame IV---------- #
        f"               .--.         ",
        f"              .sdddh/       ",
        f"              /dmmdmd       ",
        f"              `+yhhs-       ",
        f"               ./+-         ",
        f"              :hdd+`        ",
        f"             `yddd+         ",
        f"             .dmmm+         ",
        f"             `ydmms`        ",
        f"              +dmmd:        ",
        f"              `/hdy.        ",
        f"               `:md.        ",
        f"             .oyddd.        ",
        f"             .+:/my`        ",
        f"                :s:         "
    ],
    [
        # ---------Frame V----------- #
        f"                ./+/-       ",
        f"               -hdddh/      ",
        f"               :dddddo      ",
        f"               `:syy/`      ",
        f"                :oo-        ",
        f"               .dmms        ",
        f"               /mmmo        ",
        f"               +mmd+        ",
        f"               oddm+        ",
        f"               /dmdy.       ",
        f"               `ohhy.       ",
        f"               `odmd:       ",
        f"               -ddms`       ",
        f"               sdh+`        ",
        f"               so`          "
    ],
    [
        # ---------Frame VI---------- #
        f"                `://-       ",
        f"               `yddddo      ",
        f"               .dmmmmh      ",
        f"                :shyo.      ",
        f"               `-+o/        ",
        f"              `odmdy`       ",
        f"              +mmmmh.       ",
        f"              dmmmddo.      ",
        f"              hdddmshy/`    ",
        f"              :yhmm/.+s.    ",
        f"               `ommh-       ",
        f"               .hdsdy`      ",
        f"              .yd+ sd+      ",
        f"            `/hd/` .dd.     ",
        f"            .oo-    /s-     ",
    ]
]
running_frames = [
    [
        # ---------------Frame I-----------------#
        f"                .-.                   ",
        f"              -yhddy:                 ",
        f"             `ydddmmy`                ",
        f"              :yhdhy/                 ",
        f"             .-:/:.`                  ",
        f"         `-+yhdddy.   ``              ",
        f"        `sds-odmmmy-.+ys`             ",
        f"        sd/  odddyyyyy+.              ",
        f"        +:` `syyy-`..`                ",
        f"            -yyyy/`                   ",
        f"           -sy:.+ys-                  ",
        f"     ```.-ody-` `+dd:                 ",
        f"    -yhhhhy+.     /dd/                ",
        f"    `:::-.         :hh:               ",
        f"                    -hh`              ",
        f"                     ..               "
    ],
    [
        # ---------------Frame II----------------#
        f"                 `                    ",
        f"              `+yhho.                 ",
        f"              odmmdds`                ",
        f"              :hdddh/                 ",
        f"             `.://:.                  ",
        f"          `:oyhdhs`                   ",
        f"         .yh+odmmd/                   ",
        f"         sd+ sddddd/::/`              ",
        f"        .hm.`hmdm//oo+/`              ",
        f"        `:/ -hmmd-                    ",
        f"            +dd+dy-                   ",
        f"      --.``-hd+`+hh.                  ",
        f"     .yhhyyhh/` .hm+                  ",
        f"      `.:::-`   -hm/                  ",
        f"                +dd.                  ",
        f"                :o:                   "
    ],
    [
        # ---------------Frame III---------------#
        f"              -ohhs:`                 ",
        f"             -hmmmdd+                 ",
        f"             .sdmmdh-                 ",
        f"              `://:.                  ",
        f"            ./shy:                    ",
        f"           :hdmmd/                    ",
        f"          :dddmmd/                    ",
        f"          smydmdmh+.`                 ",
        f"          +dhddmh+syo`                ",
        f"          `-/dmmd/`.`                 ",
        f"         ````smddh`                   ",
        f"        .sssyhd+dd.                   ",
        f"        `/+++:.:dh.                   ",
        f"              +dd:`                   ",
        f"              /o:                     "
    ],
    [
        # ---------------Frame IV----------------#
        f"                `..`                  ",
        f"              `/hddho`                ",
        f"              -dmdmmd+                ",
        f"              `ohddhs.                ",
        f"               .:/-.`                 ",
        f"              :ydh/                   ",
        f"             :dddd:                   ",
        f"             ymmdd-                   ",
        f"             hmdmh`                   ",
        f"             omdmh-                   ",
        f"             .ydmd:                   ",
        f"              .ymds`                  ",
        f"             -+hmdy.                  ",
        f"             +hdd/`                   ",
        f"             `yd+                     ",
        f"             `//                      "
    ],
    [
        # ---------------Frame V-----------------#
        f"                 .:/:`                ",
        f"                +hdddy-               ",
        f"               `ymdddmo               ",
        f"                :syhy+`               ",
        f"                -++:`                 ",
        f"              `odmdy                  ",
        f"             `ymdmmo                  ",
        f"             :ddmdmo`                 ",
        f"             `ymddddo.                ",
        f"              :dmmh:oo                ",
        f"              `+ddy/``                ",
        f"               /hydd:                 ",
        f"              -hhodd-                 ",
        f"             :ddohdo`                 ",
        f"            :hd/.::`                  ",
        f"            `:-                       "
    ],
    [
        # ---------------Frame VI----------------#
        f"                  `:::`               ",
        f"                 /hdmdh/              ",
        f"                `ymmmdmy              ",
        f"                 -shhhs-              ",
        f"                `-/+-`                ",
        f"              `:yddds`                ",
        f"             `sdddmmy`                ",
        f"            `smsymddd/-/s+            ",
        f"            -dd-hdddooso/.            ",
        f"            -yo-ddmh-                 ",
        f"             ` +my+hh+`               ",
        f"              -dd- .sdy.              ",
        f"            `/dd/`  `ymy`             ",
        f"          -/ydy:     -dd:             ",
        f"         `sh+-`       sy-             "
    ]
]
enemies = [
    # Photo I , Beast #
    [
        f"                                              -+ydmNMNNdyo:`                MMM/   yMM         MMo                                  /MMM         :mMMMMd+.                     yMMM-      ",
        f"                                           .sNMMMmhhyyhmMMMMy:              MMM/   yMM   .+yyo-MMo :o/`+y- -oyys/`  :s+-oyyo.       /MMM        /MMMm+.                        /MMM/      ",
        f"                                         `sMMMh/`        :sNMMd-            MMM/   yMM  :NNo::sMMo oMNdss-yMy::oMm. oMMs::hMN`      /MMM       /MMMm. .mMmo`                .. -MMMy      ",
        f"                                        .mMMh.             `oMMM/           MMM/   yMM  hMy    NMo oMM.  :MMhhhhNMy oMM   -MM`      /MMM      -MMMm.  .yMMMMy:        .:+ymMMMm MMMy      ",
        f"                                        mMMs  .ymy.     :dmo :MMM-          MMM/   yMM  yMd`  .MMo oMM   .MM-```-:. oMM   -MM`      /MMM      yMMM-     .omMMMm.  `odNMMMMMMmh/ MMMy      ",
        f"                                       /MMm   .mMm.     /NMy  sMMh          MMM/   yMM  `yNmhhhmMo oMM    /dNhhdNy` oMM   -MM`      /MMM      MMMm         /ymy.  -NMMNdy+-`    MMMy      ",
        f"                                       sMMy                   /MMN          MMM/   ```    `-:. ..`  ``      .-:-`    ``    ``       /MMM      mMMM`                `..         /MMMs      ",
        f"                                       oMMd                   +MMd          MMM/                                                    /MMM/      ",
        f"                                       .NMM:     ........    `mMM+          MMM/                   :mmd/ `ommm                      /MMM      .MMMm   .ymy:                    hMMM-      ",
        f"                                        /MMM/    yyyyyyyy   -mMMy           MMM/                   -NMMMmNMMMm                      /MMM       yMMMo  .mMMMm/`     -odMN/    `yMMMd       ",
        f"                                         :mMMd/`          -yMMMo            MMM/                    `oMMMMMm/                       /MMM       `mMMM/   /yMMMNo-/ymMMMMm:   /NMMN+        ",
        f"                                          `+mMMMds+////oyNMMNs.             MMM/                     +MMMMMN.                       /MMM        .mMMMo    .sNMMMMMMMh+.   .yMMMd.         ",
        f"                                             -odNMMMMMMMMmy/`               MMM/                   .hMh/.-/mMo                      /MMM         `yMMMm/`   `+mMmy:`    `oNMMN/           ",
        f"                                                 `-MMMh.                    MMM/                   .o/     `+o                      /MMM           :mMMMNyo-.       `/osNMMNo`            ",
        f"                                                   MMMy                     MMM/  `///////:.                                        /MMM             -yNMMMMMNmmmmmmMMMMMNo`              ",
        f"                                                   MMMy                     MMM/  MMmyyyhNN+                                 yms    /MMM               /MMMmNMMMMMMMMNMMM-                ",
        f"                                                   MMMy                     MMM/  MMo    dMy   .+oso:`   .+osoo/`  ./oss+: `/dMd/-  /MMM               /MMM/         :MMMd                ",
        f"                                                   MMMy                     MMM/  MMdyyyhMd.  sNh+/sNd. -hd:.-dMs `mMo..yd+`/dMd/-  /MMM               sMMM/          hMMM/               ",
        f"                                                   MMMy                     MMM/  MMh///+hNd.-MMyyyyNMs .+sysymMh  sdmmdhs-  hMy    /MMM               yMMM           .MMMm               ",
        f"                                                   MMMy                     MMM/  MMo    /MM:-MM:...:/. yMd-.`hMh .yy..:hMN  hMy    /MMM               yMMM            sMMMo              ",
        f"                          .........................MMMh.....................MMM/  MMNmmmdmd+  +mmysymy` /mmsoodNh  odhsshd/  omNm+  /MMM...............hMMM............-NMMM-.............",
        f"                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/                                                    /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        f"                          ooooooooooooooooooooooooooooooooooooooooooooooooooooo.                                                    .ooooooooooooooooooooooooooooooooooooooooooooooooooooo"
    ],
    # Photo II , Rock #
    [
        f"                                              -+ydmNMNmdyo:                 MMM/                                                    /MMM        yMMMMm`                 oMMMMMd           ",
        f"                                           .smMMMmhyyyhmMMMNy-              MMM/                                                    /MMM        yMMMMy    -//.     ..`   :MMMMM           ",
        f"                                         `sMMMy/`        -sNMMh.            MMM/    `mm.       mm.                                  /MMM        oMMMMh   sMMMM-  .NMMM+   MMMMM           ",
        f"                                        .mMMh.              oMMN:           MMM/    .MM-   -:- MM. -- .:   -::`   .-`.::.           /MMM        /MMMMM`  +MMMN.  -MMMMs  `MMMMM           ",
        f"                                        dMMs  .ymy.     :dmo :MMM-          MMM/    .MM- /NmoohMM. MMhhy`sNyosNh` hMdsodMs          /MMM         NMMMM+   `..     .//-   /MMMMN           ",
        f"                                       /MMm   .mMm.     /NMy  sMMh          MMM/    .MM- MM.   NM. MM-  /MNyyymMs hM+  :Mm          /MMM         sMMMMm    -//////-      yMMMMy           ",
        f"                                       yMMy                   /MMN          MMM/    .MM- mM/  .MM. MM   -Mm`  -/. hM/  :Mm          /MMM         .MMMMM+  sMMMMMMMMs    .MMMMM/           ",
        f"                                       +MMh                   +MMd          MMM/    `mm. .ymmhyhm. mm    :hmddd+  sm:  -mh          /MMM          sMMMMN. +MMMMMMMM+   -mMMMMMmh+-        ",
        f"                                       `NMM:     ........    `mMM/          MMM/                                                    /MMM        `:yMMMMMm- `......` `/yMMMMMMMMMMMNy.     ",
        f"                                        :MMM/    yyyyyyyy   .mMMy           MMM/                                                    /MMM      .yNMMMMMMMMMhyoo+/+oymMMMMMMMhydMMMMMMMy`   ",
        f"                                         -mMMd/           -yMMM+            MMM/                    /MMNo`.yMMM                     /MMM    `oMMMMMMNmMMMMMMMMMMMMMMMMMMNy.   `/yMMMMMm:  ",
        f"                                           +mMMNhs+////oyNMMNs.             MMM/                    .mMMMNMMMMy                     /MMM   /NMMMMMh/  -sdmMMMMMMMMMMmy+-         :NMMMMMy`",
        f"                                             -odNMMMMMMMMmy/`               MMM/                      /MMMMMm.                      /MMM `sMMMMMm/          `.....`        ....   `yMMMMMN",
        f"                                                 `-MMMh.                    MMM/                     `yMMMMMM/                      /MMM`dMMMMMs`   .+yyyyys.             dMMMMm/`  :mMMMM",
        f"                                                   MMMy                     MMM/                    .mMs. `-dMy                     /MMMhMMMMM+   .yMMMMMMMMy             MMMMMMMN+   hMMM",
        f"                                                   MMMy                     MMM/                    ./.      :/                     /MMMMMMMM+   yMMMMMMMMMM+             dMMMMMMMMm- `yMM",
        f"                                                   MMMy                     MMM/         +MMMMMMmh-                     mM/         /MMMMMMN-   yMMMMMydMMMM/             yMMMMMMMMMM+  +N",
        f"                                                   MMMy                     MMM/         +Mm    yMd   ./++:`    -/o+:   mM/ `//`    /MMMMMN.   yMMMMM/ yMMMM/             yMMMM+hMMMMMd` .",
        f"                                                   MMMy                     MMM/         +MNooooNd:  yMs//hM+ .mN+/+Nm. mM/oNy-     /MMMMM-   .MMMMM/  mMMMM/             mMMMM/ +NMMMMm. ",
        f"                                                   MMMy                     MMM/         +MN///+NN/ :Mm   `MM yMo       mMMNN:      /MMMMy    sMMMMm   MMMMM-             MMMMM.  -NMMMMN-",
        f"                          .........................MMMh.....................MMM/         +Mm    oMh `NM:  +Md /Md. .hd. mM/`dMs     /MMMm-....NMMMMs..:MMMMM..............MMMMM....:mMMMMh",
        f"                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/         :ys    -yy  `ohddy/   -shdhs.  sy-  oyo    /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        f"                          ooooooooooooooooooooooooooooooooooooooooooooooooooooo.                                                    .ooooooooooooooooooooooooooooooooooooooooooooooooooooo"],
    # Photo III , Draco #
    [
        f"                                              -+ydmNMNmdyo:                 MMM/                                                    /MMM                 -yMMMNmmhyo:`                    ",
        f"                                           .smMMMmhyyyhmMMMNy-              MMM/                                                    /MMM                /MMmmNMMMMMMMMy.                  ",
        f"                                         `sMMMy/`        -sNMMh.            MMM/    `mm.       mm.                                  /MMM              :./dMNo`  .-/ymMMMy.                ",
        f"                                        .mMMh.              oMMN:           MMM/    .MM-   -:- MM. -- .:   -::`   .-`.::.           /MMM             sMmMd+hNNo` .+- /mMMMs               ",
        f"                                        dMMs  .ymy.     :dmo :MMM-          MMM/    .MM- /NmoohMM. MMhhy`sNyosNh` hMdsodMs          /MMMy/`          :NMMMMMMMMNo -shy:yMMMy              ",
        f"                                       /MMm   .mMm.     /NMy  sMMh          MMM/    .MM- MM.   NM. MM-  /MNyyymMs hM+  :Mm          /MMMMMNy/`        `+mMMMy:/oo    .. mMMM:             ",
        f"                                       yMMy                   /MMN          MMM/    .MM- mM/  .MM. MM   -Mm`  -/. hM/  :Mm          /MMMyNMMMNy/`       `oNMMNo`        .MMMm`            ",
        f"                                       +MMh                   +MMd          MMM/    `mm. .ymmhyhm. mm    :hmddd+  sm:  -mh          /MMM  :yNMMMMh+-      `yMMMN+        sMMMy            ",
        f"                                       `NMM:     ........    `mMM/          MMM/                                                    /MMM     :smMMMMMds/-`  -MMMM-        NMMM.           ",
        f"                                        :MMM/    yyyyyyyy   .mMMy           MMM/                                                    /MMM   ./:  -+hmMMMMMMdhyMMMM.        sMMMd       `.//",
        f"                                         -mMMd/           -yMMM+            MMM/                    /MMNo`.yMMM                     /MMM  :MMMd/`   ./oymMMMMMMMM         .MMMMmyyymmMMMMM",
        f"                                           +mMMNhs+////oyNMMNs.             MMM/                    .mMMMNMMMMy                     /MMM   omMMMMds/.    `:yydmy.          /MMMMMMMMMMmmys",
        f"                                             -odNMMMMMMMMmy/`               MMM/                      /MMMMMm.                      /MMM     :ymMMMMMMmhs/-                 .////-..`    .",
        f"                                                 `-MMMh.                    MMM/                     `yMMMMMM/                      /MMM   .yy/ ./shmMMMMMMMy                      `:/symM",
        f"                                                   MMMy                     MMM/                    .mMs. `-dMy                     /MMM   yMMMh/.   `./shmmo                    /NMMMMMMM",
        f"                                                   MMMy                     MMM/                    ./.      :/                     /MMM/   /mMMMMmy+/.`                         /NMmyo/.`",
        f"                                                   MMMy                     MMM/  .MMMMMNds-                                        /MMMMy-   -smMMMMMMMNmyyo//:                          ",
        f"                                                   MMMy                     MMM/  .MM-  `+MM/ ./:.// .+syyo-   `:+o/.    -/o+:      /MMMMMMms:`  `:+symNMMMMMMMMy                   `-//+y",
        f"                                                   MMMy                     MMM/  .MM-    yMh /MNho/ yy:.-MM. /Nd//yMy .mN+/+Nm-    /MMM/hMMMMMdy+:.    `.:/ooo+`                  -NMMMMM",
        f"                                                   MMMy                     MMM/  .MM-    hMy /Md    /ssssMM- NM-      yMo   /Mh    /MMM  `/ymMMMMMMMmyyoo+/:                      `oyyyo+",
        f"                          .........................MMMh.....................MMM/  .MMo///hMd` /Mh   /Mm  -MM- yMs  :my /Md. `hM+    /MMM......:+ydNMMMMMMMMMMy............................",
        f"                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/  `yyyyyso-   -y+   `ohdhosy-  /yddh+`  -shdhs-     /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        f"                          ooooooooooooooooooooooooooooooooooooooooooooooooooooo.                                                    .ooooooooooooooooooooooooooooooooooooooooooooooooooooo"]
]
story = [
    ["Yıllar yıllar önce, Pagenra adında bir krallık varmış. ", devam],
    ["Bu krallığın, 18 yaşına yeni adım atmış, Idren adında bir prensi varmış. ", devam],
    [
        "Ama Idren bu duruma sevinemiyormuş. Çünkü geleneğe göre 18 yaşına giren bir prens, yıllardır destanlara konu olmuş, uyuyan ejderhanın mağarasına gidip, hazinesinden bir şey almakla görevlendirilirmiş. ",
        devam],
    ["Aradan zaman geçmiş, Idren hazırlanmış ve ejderhanın inine doğru yolculuğa çıkmış. ", devam],
    ["Running\n", devam],
    [
        "Daha içine girmeden insanı ürperten bir mağaranın önünde durmuş ve meşalesini yakıp yavaşça içeri doğru yaklaşmış. ",
        devam],
    ["Ve bir anda önüne, ne olduğunu anlayamadığı bir şey çıkmış Idren'in", devam],
    ["Beast", devam],
    ["Idren yoluna şaşırmış ve yorgun bir şekilde devam etti.", devam],
    ["Walking\n", devam],
    [
        "Hiçbir şey anlayamamıştı, nasıl bir yere gelmişti, hayatında ilk defa öyle bir canlı görmüştü ( Beast'i kastederek ). Fakat buraya gelmeden önce böyle şeylerin çıkacağını söylemişti babası, kral II. Caliz. ",
        devam],
    [
        "O da zamanında buraya gelmişti, II. Caliz oradan geldikten sonra çok değişmişti, en azından halk öyle "
        "söylüyordu. ",
        devam],
    ["Daha soluk bile alamamıştı fakat önünde sanki ayakta duran bir taş bütünü gördü. ", devam],
    ["Ve bir anda bir görü gördü Idren: Önündeki şeye saldırırsa öleceğini ...", devam],
    ["Rock", devam],
    ["Biraz daha ilerledi Idren... ", devam],
    ["Walking\n", devam],
    ["Ve dillerden düşmeyen o efsanelerdeki ejderhayı gördü Idren, büyülenmişti yüceliğinden.", devam],
    ["Söylentilerdeki kadar yüceydi, güçlüydü, Draco adındaki ejderha ", devam],
    ["Draco'yu uyandırmamak için sessiz bir şekilde ileri doğru ilerledi. ", devam],
    ["Draco", devam],
    ["Başarmıştı, mağaradan bir el büyüklüğünde bir elmasla çıkmıştı Idren...", devam],
    ["Ne olur ne olmaz diye koşarak uzaklaştı mağaranın yakınlarından ", devam],
    ["Running\n", devam],
    ["Şehire geldiğinde bitap bir şekildeydi Idren, onu gören sevinç naraları atıyordu ve kalabalık artıyordu. ",
     devam],
    ["Ne de olsa prensleri, gelecek kral olmaya layık olmuştu ...\n", "Game Over :'("]]

start = input("Pagenra'ya hoş geldiniz. Oyuna başlamak için Enter'a basınız...")
system('cls')


class Idren:
    def __init__(self, health, attack, defense):
        self.name = "Idren"
        self.health = health
        self.attack = attack
        self.defense = defense


class Beast:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


class Rock:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


class Draco:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


idren = Idren(100, 50, 20)
beast = Beast("Beast the II.", 25, 10, 5)
rock = Rock("Rock", 10000, 0, 10)
draco = Draco("Draco", "?????", "?????", "?????")


def print_photo(integer):
    for i in enemies[integer]:
        print(i)


def take_enter(string, time1):
    for i in range(len(string)):
        sys.stdout.write(string[i])
        sys.stdout.flush()
        time.sleep(time1)
    inpt = input("")


def monster(monster):
    print()
    take_enter((" " * 26 + f"{idren.name}" + " " * (106 - len(str(idren.name))) + f"{monster.name}" + "\n") +
               (" " * 26 + f"Health : {idren.health}" + " " * (
                           97 - len(str(idren.health))) + f"Health : {monster.health}" + "\n") +
               (" " * 26 + f"Attack : {idren.attack}" + " " * (
                           97 - len(str(idren.attack))) + f"Attack : {monster.attack}" + "\n") +
               (" " * 26 + f"Defense : {idren.defense}" + " " * (
                           96 - len(str(idren.defense))) + f"Defense : {monster.defense}" + "\n"), 0.01)
    print()


def one_by_one(story):
    for a in range(len(story)):
        stories = story[a]
        if (stories[0] == "Beast") or (stories[0] == "Rock") or (stories[0] == "Draco") or (
                stories[0] == "Running\n") or (stories[0] == "Walking\n"):
            if stories[0] == "Beast":
                system('cls')
                print_photo(0)
                monster(beast)
                print(" " * 26 + f"1. Saldır\n" +
                      " " * 26 + f"2. Konuş\n" +
                      " " * 26 + f"3. Yandan yandan ilerlemeye ve geçmeye çalış")
                print()
                inpt = input(" " * 26 + "Yapmak istediğin : ")
                if inpt == "1":
                    print(" " * 26 + "Beast the II. : AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                    beast.health = beast.health - (idren.attack - beast.defense)
                    print(" " * 26 + f"Beast the II's Health : {beast.health}")
                    if beast.health < 0:
                        print(" " * 26 + "Beast the II. öldü...")
                elif inpt == "2":
                    take_enter((" " * 26 + "Idren : Merhaba !?"), 0.01)
                    take_enter((" " * 26 + "Beast the II. : AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 0.01)
                    print(" " * 26 + f"1. Saldır\n" +
                          " " * 26 + f"2. Yandan yandan ilerlemeye ve geçmeye çalış")
                    print()
                    inpt = input(" " * 26 + "Yapmak istediğin : ")
                    if inpt == "1":
                        print(" " * 26 + "Beast the II. : AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                        beast.health = beast.health - (idren.attack - beast.defense)
                        print(" " * 26 + f"Beast the II's Health : {beast.health}")
                        if beast.health < 0:
                            print(" " * 26 + "Beast the II. öldü...")
                    elif inpt == "2":
                        print(" " * 26 + "Beast'ın yanından yürüdün ve geçtin, kör olduğu için seni göremedi.")
                elif inpt == "3":
                    print(" " * 26 + "Beast'ın yanından yürüdün ve geçtin, kör olduğu için seni göremedi.")
                enter = input("")
                system('cls')
            elif stories[0] == "Rock":
                system('cls')
                print_photo(1)
                monster(rock)
                print(" " * 26 + f"1. Saldır\n" +
                      " " * 26 + f"3. Yandan yandan ilerlemeye ve geçmeye çalış")
                print()
                inpt = input(" " * 26 + "Yapmak istediğin : ")
                if inpt == "1":
                    print(
                        " " * 26 + "Dövüştünüz ve günler sonra bitap düştün. Öldün. Çünkü o sadece bir kayaymış. Game Over :(")
                elif inpt == "2":
                    print(" " * 26 + "Rock'ın yanından yürüdün ve geçtin, o sadece bir taşmış...")
            elif stories[0] == "Draco":
                system('cls')
                print_photo(2)
                monster(draco)
                print(" " * 26 + f"1. Saldırmak gibi bir seçeneğinin olmadığını fark ettin. Hazinesinden ses çıkarmadan bir elmas çaldın\n")
                print()
            elif stories[0] == "Walking\n":
                system('cls')
                for i in range(10):
                    for frames in walking_frames:
                        for row in frames:
                            print(" " * i * 4 + row)
                        time.sleep(.0375)
                        system('cls')
            elif stories[0] == "Running\n":
                system('cls')
                for i in range(10):
                    for frames in running_frames:
                        for row in frames:
                            print(" " * i * 8 + row)
                        time.sleep(.0375)
                        system('cls')
        else:
            for b in range(len(stories)):
                string = stories[0] + stories[1]
            take_enter(string, 0.01)


one_by_one(story)
