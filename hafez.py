#amin rezaei
#fal hafez project

import random

firstName = input("whats your name?: ")
lastName = input("whats your last name ? :")
print(f"hello {firstName}  {lastName} , Happy ancient Yalda night ")
print("Please make an intention so that I can tell you a fortune")
answer = str(input("If you are ready, let's start. yes or no?"))

if answer == "yes" :

  hafez = [
    'الا یا ایها الساقی ادر کاسا و ناولها / که عشق آسان نمود اول ولی افتاد مشکل‌ها',
    'صلاح کار کجا و من خراب کجا / ببین تفاوت ره کز کجاست تا به کجا',
    'اگر آن ترک شیرازی به دست آرد دل ما را / به خال هندویش بخشم سمرقند و بخارا را',
    'صبا به لطف بگو آن غزال رعنا را / که سر به کوه و بیابان تو داده‌ای ما را',
    'دل می‌رود ز دستم صاحب دلان خدا را / دردا که راز پنهان خواهد شد آشکارا',
    'به ملازمان سلطان که رساند این دعا را / که به شکر پادشاهی ز نظر مران گدا را',
    'صوفی بیا که آینه صافیست جام را / تا بنگری صفای می لعل فام را',
    'ساقیا برخیز و درده جام را / خاک بر سر کن غم ایام را',
    'رونق عهد شباب است دگر بستان را / می‌رسد مژده گل بلبل خوش الحان را',
    'دوش از مسجد سوی میخانه آمد پیر ما / چیست یاران طریقت بعد از این تدبیر ما',
    'ساقی به نور باده برافروز جام ما / مطرب بگو که کار جهان شد به کام ما',
    'ای فروغ ماه حسن از روی رخشان شما / آب روی خوبی از چاه زنخدان شما',
    'می‌دمد صبح و کله بست سحاب / الصبوح الصبوح یا اصحاب',
    'گفتم ای سلطان خوبان رحم کن بر این غریب / گفت در دنبال دل ره گم کند مسکین غریب',
    'ای شاهد قدسی که کشد بند نقابت / و ای مرغ بهشتی که دهد دانه و آبت',
    'خمی که ابروی شوخ تو در کمان انداخت / به قصد جان من زار ناتوان انداخت',
    'سینه از آتش دل در غم جانانه بسوخت / آتشی بود در این خانه که کاشانه بسوخت',
    'ساقیا آمدن عید مبارک بادت / وان مواعید که کردی مرواد از یادت',
    'ای نسیم سحر آرامگه یار کجاست / منزل آن مه عاشق کش عیار کجاست',
    'روزه یک سو شد و عید آمد و دل‌ها برخاست / می ز خمخانه به جوش آمد و می باید خواست'
  ]

  print("here you are this the fortune that has fallen to your lot")

  print(random.choice(hafez))
else :
 print("We will wait until you are ready")
