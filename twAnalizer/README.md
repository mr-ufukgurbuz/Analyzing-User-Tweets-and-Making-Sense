# CSE4095S18_Group4
### Data Science Course Project - Analizer

## ----- (1) For the whole dataset -----

```
----- (1) For the whole dataset -----

a. total number of instances: 858

b. average length of instances in characters: 129.80769230769232

c. std dev of length of instances in characters: 60.58645008381157

d. average length of instances in words (after tokenization): 6.058930602957907

e. std dev of length of instances in words (after tokenization): 3.0830463101059733

f. the most frequent 10 words:
      Word  Frequency
0        8        190
1  TÜBİTAK        153
2      MAM        120
3  Türkiye         57
4    Afrin         52
5       Dr         52
6  Başkanı         36
7     Prof         35
8  AACanli         34
9  dünyaya         32

![alt text](https://user-images.githubusercontent.com/16938791/39147492-6c389bf6-4742-11e8-80a7-327ce221447c.png "The Most Frequent 10 Words")

g. the most frequent 50 words:
                  Word  Frequency
0                    8        190
1              TÜBİTAK        153
2                  MAM        120
3              Türkiye         57
4                Afrin         52
5                   Dr         52
6              Başkanı         36
7                 Prof         35
8              AACanli         34
9              dünyaya         32
10             İbrahim         27
11           Araştırma         25
12             Projesi         24
13              Bakanı         24
14                 ABD         23
15                  11         22
16          Kılıçaslan         22
17            İstanbul         22
18           Çalıştayı         22
19                 PKK         21
20                   9         20
21           Enstitüsü         20
22                  12         19
23                   5         18
24                   7         17
25               Genel         17
26  ZeytinDalıHarekatı         17
27                  10         16
28                 Bşk         16
29             MARMARA         16
30              Enerji         15
31              Ankara         15
32                   4         14
33             Merkezi         14
34             Marmara         14
35          Toplantısı         14
36             MERKEZİ         14
37            Başbakan         14
38           ARAŞTIRMA         14
39                  13         13
40              Örgütü         13
41               Terör         13
42                Türk         13
43           Dışişleri         13
44               Deniz         12
45          Fetullahçı         12
46             Malzeme         11
47              Sanayi         11
48              Zeytin         11
49                Dalı         11

![figure_2](https://user-images.githubusercontent.com/16938791/39147501-73c00e22-4742-11e8-98c9-881d37489717.png)

h. number of instances that are less than 5 characters: 1392 
```

## ----- (2) For each class label -----

```
----- (2) For each class label -----

a. total number of instances:
 {'dateCount': 601, 'compCount': 1178, 'eventCount': 843, 'contactCount': 9, 'jobCount': 540, 'idCount': 54, 
 'ageCount': 0, 'placeCount': 538, 'trashCount': 0, 'nameCount': 592, 'addressCount': 40}

b. average length of instances in characters:
 {'avgLengthOfContact': 3.18181, 'avgLengthOfName': 6.19528, 'avgLengthOfID': 8.3214, 'avgLengthOfJob': 6.4870, 
 'avgLengthOfAge': 0, 'avgLengthOfAddress': 5.85714, 'avgLengthOfTrash': 0, 'avgLengthOfPlace': 6.6444, 
 'avgLengthOfComp': 6.2822, 'avgLengthOfEvent': 7.3242, 'avgLengthOfDate': 2.4809}

c. std dev of length of instances in characters:
 {'stdDevOfDate': 1.889, 'stdDevOfID': 3.057, 'stdDevOfAge': 0.0, 'stdDevOfComp': 2.703, 'stdDevOfContact': 2.315, 
 'stdDevOfName': 2.460, 'stdDevOfTrash': 0.0, 'stdDevOfEvent': 3.358, 'stdDevOfAddress': 2.514, 'stdDevOfPlace': 2.458, 
 'stdDevOfJob': 2.935}

f. the most frequent 10 words:

------ Event ------

                 Word  Frequency
0             Projesi         22
1           Çalıştayı         22
2  ZeytinDalıHarekatı         16
3          Toplantısı         14
4              Zeytin         11
5            Harekatı          9
6                Dalı          9
7              Töreni          7
8              Ulusal          7
9           Araştırma          7 


------ Trash ------

[None] 


------ Address ------

           Word  Frequency
0       Türkiye          6
1         Afrin          6
2           ABD          3
3        Ankara          1
4          Irak          1
5  kaybettikten          1
6     Denizlili          1
7     Şanlıurfa          1
8   Ceylanpınar          1
9       Belarus          1 


------ ID ------

                 Word  Frequency
0             AACanli         30
1         TUBITAK_MAM          2
2  enerjiarzguvenligi          1
3         halukgorgun          1
4         cengiztomar          1
5             TCBEBKA          1
6       lipiindonesia          1
7       Dr_Faruk_Ozlu          1
8             Tubitak          1
9           İslamabad          1 


------ Comp ------

        Word  Frequency
0    TÜBİTAK        146
1        MAM        117
2  Enstitüsü         20
3        PKK         20
4  Araştırma         18
5    MARMARA         16
6    MERKEZİ         14
7  ARAŞTIRMA         13
8    Marmara         12
9     Örgütü         12 


------ Age ------

[None] 


------ Place ------

         Word  Frequency
0     Türkiye         45
1       Afrin         44
2     dünyaya         32
3         ABD         19
4    İstanbul         13
5      Ankara          9
6       Rusya          7
7        İran          7
8      İsrail          6
9  Yunanistan          5 


------ Contact ------

      Word  Frequency
0     ctue          1
1      641          1
2  Başkent          1
3       19          1
4     2900          1
5      262          1
6       tr          1
7      gov          1
8  TÜBİTAK          1 


------ Name ------

                   Word  Frequency
0               İbrahim         27
1            Kılıçaslan         22
2               Mustafa         10
3             Çavuşoğlu         10
4               Erdoğan          9
5                Bozdağ          8
6                 Hasan          8
7  CumhurbaşkanıErdoğan          7
8                 İlhan          6
9                 Aydın          5 


------ Date ------

   Word  Frequency
0     8        188
1    11         22
2     9         20
3    12         18
4     5         17
5     7         17
6    10         15
7     4         14
8    13         13
9     6         10 


------ Job ------

         Word  Frequency
0          Dr         52
1     Başkanı         36
2        Prof         35
3      Bakanı         24
4         Bşk         16
5    Başbakan         14
6       Genel         13
7   Dışişleri         12
8   sanatçısı          8
9  Yardımcısı          8 


g. the most frequent 50 words:

------ Event ------

                  Word  Frequency
0              Projesi         22
1            Çalıştayı         22
2   ZeytinDalıHarekatı         16
3           Toplantısı         14
4               Zeytin         11
5             Harekatı          9
6                 Dalı          9
7               Töreni          7
8               Ulusal          7
9            Araştırma          7
10               Eylem          6
11        Uluslararası          5
12                Ödül          5
13             Merkezi          5
14           Havacılık          5
15                Expo          5
16              Enerji          5
17                Test          5
18                2016          5
19                  Ge          4
20                  Ar          4
21             Organik          4
22               Etüdü          4
23          Fizibilite          4
24                Günü          4
25            Planının          4
26                 CEV          4
27               Proje          4
28               Helal          4
29              Destek          4
30             Kapanış          4
31           Güvenliği          4
32       Teknolojileri          4
33                  Su          4
34                2017          4
35              Akıllı          3
36         Kümelenmesi          3
37                 MAM          3
38             TÜBİTAK          3
39             Türkiye          3
40       Güncellenmesi          3
41             Eğitimi          3
42                 Arz          3
43        Belirlenmesi          3
44               canlı          3
45        Hareketlilik          3
46             Yönelik          3
47          Konferansı          3
48               diyen          3
49              Kupası          3 


------ Trash ------

[None] 


------ Address ------

            Word  Frequency
0        Türkiye          6
1          Afrin          6
2            ABD          3
3         Ankara          1
4           Irak          1
5   kaybettikten          1
6      Denizlili          1
7      Şanlıurfa          1
8    Ceylanpınar          1
9        Belarus          1
10           Çin          1
11         Deniz          1
12        Bartın          1
13         Darah          1
14    Yunanistan          1
15           Ayn          1
16        Sincar          1
17          Burj          1
18      Abdallah          1
19       Basutah          1
20         İdlib          1
21        Münbiç          1
22        Kıbrıs          1
23        Suriye          1
24         Idlib          1
25    Çeçenistan          1
26         Gazze          1
27       Kayseri          1 


------ ID ------

                  Word  Frequency
0              AACanli         30
1          TUBITAK_MAM          2
2   enerjiarzguvenligi          1
3          halukgorgun          1
4          cengiztomar          1
5              TCBEBKA          1
6        lipiindonesia          1
7        Dr_Faruk_Ozlu          1
8              Tubitak          1
9            İslamabad          1
10          haydaroruc          1
11          isdb_group          1
12           UFUK_2020          1
13            GtuEduTr          1
14         12numaraorg          1
15     TubitakKitaplar          1
16         MSI_Dergisi          1
17       muratyesiltas          1
18            TCSanayi          1
19     TUBA_TurkBlmAkd          1
20         ECO4Science          1
21              sesric          1
22         Tika_Turkey          1
23             aa_spor          1 


------ Comp ------

             Word  Frequency
0         TÜBİTAK        146
1             MAM        117
2       Enstitüsü         20
3             PKK         20
4       Araştırma         18
5         MARMARA         16
6         MERKEZİ         14
7       ARAŞTIRMA         13
8         Marmara         12
9          Örgütü         12
10          Terör         12
11        Malzeme         11
12     Fetullahçı         11
13            TSK         10
14           Türk          9
15        Merkezi          9
16         Enerji          9
17           FETÖ          9
18            YPG          8
19        tubitak          7
20      Bakanlığı          7
21       İstanbul          7
22         Heyeti          6
23       Kalkınma          6
24         Ajansı          6
25            PYD          6
26          Deniz          5
27         Sanayi          5
28       gazetesi          5
29     Cumhuriyet          5
30        Bankası          5
31             AA          5
32            ÖSO          5
33          Genel          4
34         Avrupa          4
35        Kocaeli          4
36           Bank          4
37         Ziraat          4
38        Çiftlik          4
39      Müdürlüğü          4
40           Gıda          4
41           TBMM          4
42            PDY          4
43        Tersane          4
44       Facebook          4
45        YouTube          4
46         Sağlık          4
47  Biyoteknoloji          4
48        AACanli          4
49   Üniversitesi          4 


------ Age ------

[None] 


------ Place ------

             Word  Frequency
0         Türkiye         45
1           Afrin         44
2         dünyaya         32
3             ABD         19
4        İstanbul         13
5          Ankara          9
6           Rusya          7
7            İran          7
8          İsrail          6
9      Yunanistan          5
10           Doğu          5
11      İngiltere          5
12             15          4
13           Guta          4
14       Şehitler          4
15        Köprüsü          4
16            Çin          4
17         Suriye          4
18         Temmuz          4
19          Konya          4
20         Kıbrıs          4
21        Amerika          3
22         Fransa          3
23      Arabistan          3
24          Suudi          3
25        Kocaeli          3
26          Gebze          3
27          Gediz          2
28        İspanya          2
29         Münbiç          2
30        Almanya          2
31           TBMM          2
32       Pakistan          2
33        Kahvesi          2
34           Ağrı          2
35     Filistinli          2
36            köy          2
37       Hollanda          2
38          Sinop          2
39          Gazze          2
40           Ülke          2
41         Rumeli          2
42          Adası          2
43      Ülkemizin          2
44        Dünyada          2
45       Filistin          2
46       Tebessüm          2
47          Münih          2
48         Avrupa          2
49  cezaevlerinde          2 


------ Contact ------

      Word  Frequency
0     ctue          1
1      641          1
2  Başkent          1
3       19          1
4     2900          1
5      262          1
6       tr          1
7      gov          1
8  TÜBİTAK          1 


------ Name ------

                    Word  Frequency
0                İbrahim         27
1             Kılıçaslan         22
2                Mustafa         10
3              Çavuşoğlu         10
4                Erdoğan          9
5                 Bozdağ          8
6                  Hasan          8
7   CumhurbaşkanıErdoğan          7
8                  İlhan          6
9                  Aydın          5
10                Baykal          5
11                 Celal          5
12                İsmail          5
13                 Trump          5
14                 Deniz          5
15                 Kemal          4
16          Kılıçdaroğlu          4
17                  Aşık          4
18                Mehmet          4
19                  Özlü          4
20               Atatürk          4
21                Veysel          4
22                 Faruk          4
23                 Ahmet          3
24             Hayrettin          3
25                 Güzel          3
26                  Arif          3
27                Sultan          3
28               Hüseyin          3
29                   Ali          3
30               Kandili          2
31                Münbiç          2
32                   Gül          2
33                Pompeo          2
34                 Abbas          2
35              Yıldırım          2
36      BaşbakanYıldırım          2
37                  Alim          2
38               Karagöz          2
39                Bülent          2
40                 Aksoy          2
41              Süleyman          2
42              Zeybekci          2
43                Ferhat          2
44                Selman          2
45                  Sami          2
46                  Akar          2
47                  YULA          2
48                 Aylin          2
49                  Özer          2 


------ Date ------

      Word  Frequency
0        8        188
1       11         22
2        9         20
3       12         18
4        5         17
5        7         17
6       10         15
7        4         14
8       13         13
9        6         10
10      14          9
11    1982          6
12      15          5
13   Bugün          5
14    1923          5
15    1936          5
16    1971          5
17    2017          5
18       3          4
19   bugün          4
20    1925          4
21    1974          4
22    1975          4
23    1995          4
24    2013          3
25    1915          3
26    1984          3
27    1924          3
28    1928          3
29    1934          3
30    1944          3
31    1949          3
32    1964          3
33    1972          3
34    1976          3
35    1980          3
36    1985          3
37    1986          3
38    1987          3
39    1988          3
40    1997          3
41    2000          3
42    1921          2
43    1992          2
44    1989          2
45    1912          2
46    1929          2
47    1940          2
48  Temmuz          2
49    1950          2 


------ Job ------

             Word  Frequency
0              Dr         52
1         Başkanı         36
2            Prof         35
3          Bakanı         24
4             Bşk         16
5        Başbakan         14
6           Genel         13
7       Dışişleri         12
8       sanatçısı          8
9      Yardımcısı          8
10  Cumhurbaşkanı          8
11       futbolcu          7
12          yazar          7
13         yazarı          6
14         Sanayi          6
15       Komutanı          5
16      Teknoloji          5
17          Bilim          5
18         oyuncu          4
19          hakim          4
20      Sekreteri          4
21         Müdürü          4
22         sinema          4
23           Paşa          4
24           şair          4
25        şarkıcı          3
26         Ankara          3
27   Milletvekili          3
28         Kurulu          3
29       askerini          3
30       gazeteci          3
31    Büyükelçisi          3
32   Danışmanları          3
33       Gazeteci          3
34        Yönetim          3
35         Valisi          3
36        Tiyatro          3
37         ressam          3
38         aktris          3
39           köşe          2
40        tiyatro          2
41         emekli          2
42      Müsteşarı          2
43    Araştırmacı          2
44     Korgeneral          2
45    akademisyen          2
46       Askerler          2
47      büyükelçi          2
48            Doç          2
49   başkanlığına          2 


h. number of instances that are less than 5 characters:

Trash Count:      0
Event Count:      146
Name Count:       86
Address Count:    7
Date Count:       571
Comp Count:       343
Age Count:        0
Job Count:        147
Place Count:      85
Contact Count:    7
ID Count:         0

Process finished with exit code 0
```


