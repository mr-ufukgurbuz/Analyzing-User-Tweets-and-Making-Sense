# CSE4095S18_Group4
### Data Science Course Project


Merhaba arkadaşlar, 

Öncelikle sağlamış olduğu arayüz programından dolayı <b>'Murat'</b> kardeşime ve bu arayüzün kullanımı için RESTful web servis yazan <b>'Fatih'</b> kardeşime teşekkür ederim.

Yazılmış olan bu web servis üzerinden etiketleme yapılırken, tüm grup üyelerinin kendi bilgisayarına <i>'MongoDB database'</i> ve python kodunun ilgili <i>'library'</i> lerini kurması gerekmektedir. Ayrıca, her grup üyesinin yaptığı etiketlemeler kendi bilgisayarındaki veritabanına kaydedilecek ve daha sonra birleştirilmesi gerekecektir.  Özellikle <b>'NER'</b> projesi yapan arkadaşlar için, yüzlerce kullanıcının binlerce tweet'i için <i>'tweet tekrarı'</i> olmamasına dikkat etmek v.s sıkıntı olacaktı bizim için. Ben de bu arayüzü bir tık daha geliştirerek kullanım kolaylığı sağlaması için 'web ortamına' taşıdım. Ve hatalı tweet etiketlemelerinde, önceki 'tweet'lerin düzeltilmesi için arayüze bir 'previous' butonu koydum. Böylelikle daha önceki etiketlemeleri tek bir başlık altında görebileceğiz.

## Remote Database Part

Arkadaşlarımızın yazdığı arayüz ve web servisi <b><i>'remote'</i></b> ortama taşıyarak grup içi ortak bir kullanıma sunabiliriz. Öncelikle "MongoDB database" için 'ücretsiz 500 mb' depolama alanı sağlayan "mLab" (https://mlab.com/) sitesine kayıt oluyoruz. Kayıt olduktan sonra yeni bir 'database' yaratıyoruz ve tweet'lerimizi depolayacağımız 'collection' ımızı oluşturuyoruz. Daha sonra bu database için bir 'kullanıcı' tanımlıyoruz. Database erişim bilgileriniz aşağıdaki gibidir.

![mlab_remote_database](https://user-images.githubusercontent.com/16938791/37683529-f49ae1e4-2c9d-11e8-804a-2a9e19aca294.PNG)

## Remote Python Web Service Part

Python kodumuzu remote bir instance üzerinde çalıştırmak için 'DigitalOcean', 'GCP' gibi birçok 'compute provider' kullanabiliriz. Fakat, bunların aksine web projelerinin daha hızlı test edilmesi için kullanıcılan 'Heroku' yu öneririm. Öncelikle, 'Heroku'ya (https://www.heroku.com/) kayıt oluyoruz ve ücretsiz kullanım olan 'Sandbox' kurulum paketini seçiyoruz. İnternet üzerinde kurulum ile ilgili 2 dklık kısa videolar bulabilirsiniz. Kurulumdan sonra, ilk 'app'imizi oluşturuyoruz. Bu 'app'i oluştururken mümkün olduğunca anlamsız ve uzun bir isimlendirme yapalım('Güvenlik gereği'). Bu isim bizim daha sonra 'URL' üzerinden 'app'e erişmemizi sağlayacak, üçüncü şahısların erişmesini istemeyiz.

Daha sonra 'app'imizin çalıştıracağı uygulamamızın türünü belirtmek için, ayarlar sekmesinden <b>'settings'</b> diyerek, <b>'Buildpacks'</b> bölümünden <i>'Add builpack'</i> diyelim  ve <b>'Python'</b> seçelim.

Daha sonra yine aynı <b>'settings'</b> sekmesinden, <b>'Config Variables'</b> bölümünden <b>'Reveal Config Vars'</b> diyelim ve instance'ımız için <i>'ortam değişkenlerini'</i> aşağıdaki gibi atayalım.  Bu şekilde, 'Twitter' hesap key'lerimizi ve 'database' erişim bilgilerimizi 'python kod' içerisinde açık olarak saklamak yerine daha güvenli bir şekilde tutabiliyoruz.

![heroku_instance_environment_variables](https://user-images.githubusercontent.com/16938791/37684648-c44b35e4-2ca1-11e8-86ea-f578cb6f1ae7.PNG)


Daha sonra <b>'bu repodaki kodu'</b>, kendi Github hesabımıza klonluyoruz.

### Note: İçerisinde size anlamsız gelen ve proje ile ilgisi olmayan dosyaları silmeyin! Bunlar 'Heroku' için gerekli olan dosyalar". 'requirements.txt' dosyası içerisinde, projede kullanılan 'python library'leri tanımlanmıştır. Sizin ekstra olarak başka library'leriniz varsa buraya yazabilirsiniz. 'Heroku', bunları da sizin için yükleyecektir.

Klonlama işleminden sonra ayarlar sekmesinden <b>'Deploy'</b> diyerek, <b>'Deployment method'</b> bölümünden 'Heroku' ile 'Github' hesabımızı birbirine bağlıyoruz. Böylece 'Heroku' direkt 'Github'dan kodumuzu çekebilecek.

Son olarak yine aynı <b>'Deploy'</b> sekmesindeki, <b>'Manual deploy'</b> bölümünden <b>'Deploy Brach'</b> diyoruz. Böylece, 'Heroku' 'Github'dan kodumuzu çekiyor ve 'requirements.txt' dosyasındaki 'python library'lerini kuruyor. Deploy sonucunda 'view' butona tıklamamız sonucu ortaya çıkan 'unique URL' bizim 'app'imize erişimizi sağlayacak. Bu 'URL' ile cep telefonlarından <b>'dersteyken'</b> bile etiketleme yapabilirsiniz. Artık 'app'imiz kullanıma hazır. <b> Afiyet olsun.. :)</b>

![web_application_screenshot](https://user-images.githubusercontent.com/16938791/37685742-a081e6a4-2ca5-11e8-80d6-f4394e2858ff.PNG)

