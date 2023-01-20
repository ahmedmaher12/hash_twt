update_version = 1
import json
import requests
import random
import sys
import time
import os
import urllib3


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



Auto_Login_Email = ''
Auto_Login_PASSWORD = ''
print(f'{bcolors.HEADER}[*] Script version ===> [2.8]{bcolors.BOLD}')
print(f'{bcolors.OKGREEN}[*] Now I ComeBack{bcolors.BOLD}')
time.sleep(2)
print(
    f'{bcolors.WARNING} لو في اي مشكلة في الاسكريبت ابعت علي جروب احنا شايفنكوا و معاكوا و هنفضل ديما معاكوا [*] {bcolors.BOLD}')
print('[*] لو مش هياخد من وقتك حاجة ف ياريت تستغفر ربنا و لو ينفع ف ممكن تدعيلي و شكرا ليك')

Hashtag_res = requests.get('https://hashtag-changer-default-rtdb.firebaseio.com/save_hashtag.json')
data_of_Hashtag = json.loads(Hashtag_res.content.decode('UTF-8'))

Hashtag = data_of_Hashtag['Hashtag']
script_state = data_of_Hashtag['Script']

print(Hashtag)
if script_state == 'Run':
    print(f'{bcolors.OKGREEN}[*] Admins open Script{bcolors.BOLD}')
else:
    print(f'{bcolors.FAIL}[*] Admins close Script{bcolors.BOLD}')
    sys.exit()
arr = ['A year from now you may wish you had started today.\n', 'Keep going.\n', 'Actions speak louder than words.\n',
       'Every new day is another chance to change your life\n', 'مش هنسكت مهما عملتو!!!!!\n',
       'Whatever you did trying to stop us, you will never succeed\n', 'قاطع الحراميه النت مش سلعة استهلاكيه \n',
       'مش هنسكت و مش هنرضي غير ب نت غير محدود و سرعات كويسه\n', 'عاش يوحوش خلي عندكم اصرار واوعوا تترجعوا\n',
       "don't stop\n", 'بس لازم مقاطعه أو محدش يجدد خالص\n',
       'هتفضلو تسكتوا و تضحكوا و تستغلوا وتسرقوا الشعب لغاية ما هينفجر فيكم مرة واحدة\n',
       'i wonder there is people working for thier customers but in Egypt they are working for (stealing your money not to you )\n',
       'محدش يستسلم\n', 'المرادي مفيش رجوع\n', 'لسا بدري بس مش هنكسل\n',
       'ليه ميبقش عندنا انترنت شبه اي دولة احنا مش اقل من اي دولة في العالم و لو المسئوليين مش عارفيين يحلو الموضوع يمشو احسن حقنا فى ام الدنيا\n',
       'حقنا فى ام الدنيا\n', 'ازاي بتقول مفيش بنية تحتية كويسة واحن كل شهر بنجدد و بتستحمل عادي ؟\n',
       'يا مسهل الحال يارب\n', 'احنا مش هنسكت لغاية ما كل المصريين يبقى عندهم نت كويس و غير محدود و رخيص\n',
       'نعم لالغاء باقة ال140 جيجا\n', 'النهاية قريبة @telecomegypt\n', 'مفيش يأس مكمليييين\n',
       'من حقنا دولة من اهم اهم دول الشرق الاوسط ازي مكنتش الاهم بانترنت غير محدود و سريع\n',
       'الغاء سياسة الاستخدام العادل\n',
       'بعد كل المليارات الي دفعتوها عشان نقع تفتكر وقعنا هههه ابلع الهاشتاج ده ينرم\n',
       'ونت بتكتب تويتات كل شويا خد بالك من الناس اللي شغاله بالاسكريبت اتفاعل معاهم عشان تعلي اكتر وتتحسب التويته بتاعتهم\n',
       'مش ها نسكت عن حقنا تاني أبداً\n', 'ده حقنا مش هنسيبوا\n', 'ان شاء الله حناخد حقنا وانتم قدها\n',
       'ليه ميبقش عندنا انترنت شبه اي دولة احنا مش اقل من اي دولة في العالم و لو المسئوليين مش عارفيين يحلو الموضوع يمشو احسن\n',
       'انا على اخري حقيقي\n',
       'مصلحتنا في انترنت سريع غير محدود و موفر يخدم اهداف الجمتمع المصري في كل المجالات سواء تعليمية او ترفيهية او تجارية او عملية النت اصبح ضرورة اساسية مش ثانوية\n',
       'مش عايزين ده يقع\n', 'يارب يفضل مركز اول\n',
      "Don't stop asking for ur rights u can change the future keep fighting like a wirror this is ur war and u can win it and u will win it\n",
       'لازم نهد المعبد علي دماغهم\n', 'We can win this\n', 'مش هنوقف مهما حصل عشان الكل جاب اخره\n',
       'بلاش احتكار وخلوا الناس تاخد حقها\n',
       'مكمل معاكم شاحن كرت ب ١٠ جنيه ومش هجدد الباقة لما نشوف آخرهم معانا ايه\n',
       'السرقة عندكوا اسلوب حياة @telecomegypt\n', 'عاش\n', 'مستمرين قاطعوهم\n',
       'مش كفاية سبوبة التلفون الارضي المحدش بيستخدمه وبيدفع تمنه اجباري ياعني الباقة وقفة علينا اغلي من سعرها بطلو بق شغل العصابات و الحرامية و كماية النصب ده\n',
       'الانترنت مش سلعة\n', 'هنفلسكم يا شركة وي\n', 'هنفضل لحد اخر نفس فينا\n',
       'ما تدوا الناس نت غير محدود ايه الرخامة دي !!!\n', 'مش عايزين يعملوا الانترنت محدود لان السبوبه هتضيع عليهم\n',
       'ده حقنا\n',
       'بنطلب تقل حق لينا مع ذلك كلهم ضدنا بحجة ان مفيش بنية تحتية.. بس البنية التحتية تتحمل اجدد اكتر من مرة فى الشهر عادى\n',
       'مكملين وراهم لغاية يحققوا حلمنا\n', 'اجمدواا\n', 'كملواا\n', 'انا كل اللي اقدر عليه اشارك معاكم الهاش\n',
       'محدش يستستلم\n', 'كملوا يا شباب\n', 'بسم الله، نبدأ\n', 'ما حدش يستسلم\n',
       'وقالوا حسبنا الله سيؤتينا الله من فضله ان الى الله راغبون\n', 'كملوااااا\n',
       'الغلطة غلطتنا من البداية، اننا سمحنا بالباقات\n', 'كملوا\n', 'فعل فعل\n',
       'كملوا يا شباب مش اقل من حد والله لازم نستمر في الضغط، لازم يخسروا عشان يحسوا\n', 'والله الباقة خلصت ومش هجدد\n',
       'كله يقاطع كل الشركات مش وي بس، لما الشركات الباقية توافق ع سياستهم القذرة تبقى شريكة في الجريمة\n',
       'لو كان من الصعب توفير انترنت بلا حدود بسبب البنية التحتية، اومال كنتوا بتعملوا ابه طول السنين اللي فاتت، مش كفاية جشع وحب المال والسلطة ده كله هتسيبوه ورا ضهركم وهنشيلكم في توابيت\n',
       'هو يعني ايه باقة ١٤٠جيجا ولو خلصت السرعة تنزل الى ٢٥٦ ومش بتوصل كاملة\n', 'الترند بيقع يا جماعة كملوا\n',
       'ده حقنا كلنا\n', 'محدش يسكت عن حقه\n', 'حسبي الله ونعم الوكيل فيكم\n', 'كملوا للآخر يا شباب\n',
       'اليأس ضعف جبان، كملوا يا شباب\n', 'مش هنقبل بأقل من انترنت بلا حدود\n',
       'لازم نستمر لغاية ما نشوف انترنت بلا حدود\n', 'لازم كله يقاطع الشركات دي، لأن هما اللي محتاجينك مش انت\n',
       'بطلوا سرقة يا شركة حرامية\n', 'كله يقاطع شركات الاتصالات ده الحل\n', 'Never give up, Never give up\n',
       'استغفر الله واتوب اليه\n', 'بطلوا جشع كفاية بقى\n', 'يا رب انترنت بلا حدود\n', 'يا رب ادينا من فضلك\n',
       "They are treating us like slaves, this won't last\n",
       'ولو أنهم رضوا ما آتاهم الله ورسوله وقالوا حسبنا الله سيؤتينا الله من فضله ورسوله إنا إلى الله راغبون\n',
       '" الشيطان يعدكم الفقر ويأمركم بالفحشاء والله يعدكم مغفرة منه وفضلا والله واسع عليم "\n', 'كله يكمل\n',
       'محدش يمل\n', 'ومن يتقي الله يجعل له مخرجا، ويرزقه من حيث لا يحتسب\n', 'لازم كله يقاطع كل الشركات القذرة دي\n',
       'طيب وبعدين يا شباب في ولاد الذين دول\n',
       'Most of our needs depends on the internet, like studying, shopping, entertainment, and more, go to the hell "We company" and everyone supporting you.\n',
       'بيعاملوا الجيجا ع اساس انها طماطم وبطاطس\n', 'this is uor chance\n', 'Keeeeep goooooing\n',
       'ما تتفاعلوا هو انتوا نمتوا ده حقنا كلنا فوقوا وكفاية استغفال\n', 'WE CAN DO IT\n', 'Hi There\n',
       'يا رب ما اعظمك\n', 'لا اله إلا انت سبحانك اني كنت من الظالمين\n', '"من تعجل شيئاً قبل أوانه عوقب بحرمانه"\n',
       'مكملين بإذن الله، حتى تتخقق غايتنا\n', 'Keeep gooing\n',
       'والله صدق الشيخ عبد الحميد كشك لما قال، "تسعة أعشار الظلم في مصر ، والعُشر الأخير يجوب العالم نهاراً ، ويبيت ليلته في مصر"\n',
       'انت مش لوحدك كلنا معاك\n', 'لا تراجع ولا استسلام\n', 'يجب مقاطعة وي وكل الشركات بقوة\n',
       "Just don't stop, and keep going\n", 'ازاي مصر الدولة الوحيدة اللي فيها الانترنت محدود\n',
       'والله يا جماعة لو مشترك انا اول واحد هلغي وهقاطع كل الشركات مش بس وي، لأن باقي الشركات مشتركين في الجريمة\n',
       'بطلوا سرقة بقى\n', 'نت بلا حدود\n', 'هدفنا مش خدمتك هدفنا شرقتك\n', 'لازم انترنت بلا حدود\n',
       'This company is worst ever\n', 'مش لاقي كلام اقوله\n', 'للمرة ال ٥،٠٠٠ انترنت بلا حدود\n',
       'بطلوا سرقة، وخلوا الانترنت بلا حدود، اومال كنتوا بتعملوا ايه الفترة دي بالفلوس\n', 'بطلوا جشع\n',
       'دي سرقة علني\n', 'لا يأس مش الحياة ولا حياة مع اليأس\n', 'Never give up bro\n', 'يا مسهل\n', 'كفاية سرقة\n',
       'يجدع في ناس بتستلف من هنا ومن هنا  علشان تدخل نت لاجل عيالها عشان يتعلموا وميعرفوش انها منظومه فاشله  ف ظل ان كل حاجه بتغلي والنت نفسو بقي اسرع علشان الباقه تخلص ونجدد تاني والمواطن الغلبان هوا اللي ضايع ف الرجلين شكرا\n',
       'Stop selling No more limited internet\n', 'كله يكمل كله يكمل دي فرصتنا لو ضاعت هنفضل طول عمرنا كده \n',
       'حرام لما اوقف كل التحديثات عشان خايف الباقة تخلص، حسبي الله ونعم الوكيل فيكم واحد واحد\n',
       'Together we can do the impossible\n', 'الانترنت اصبح شيء اساسي في حياتنا\n',
       'انا بجد مش متخيل اننا الوحيدون اللي عندنا نت محدود\n', 'we are the strong side\n',
       'لازم يكون عندنا نت بلا حدود زي البشر\n', 'لازم يكون عندنا نت بلا حدود \n', 'لا حول ولا قوة الا بالله\n',
       'ازاي ازاي ازاي احنا في ٢٠٢٢ والنت لسه محدود في مصر ده عار علينا\n',
       'يعني ايه اسرع دولة في افريقيا والنت محدود، ده استخفاف بالعقول\n', 'go on\n', 'مش كفاية احتكار\n',
       'مش كفاية سرقة، اعملوا حاجة كويسة لآخرتكم\n', 'مش كفاية جشع, مش كفاية جشع\n',
       'شركة مش عندها اي نوع من الادمية\n', 'خلص الكلام\n',
       'Egyptians fight for their rights as any citizen in his country all over the world\n', 'انا هنا معاك وبدعمك\n',
       'دوام الحال من المحال\n', 'حد يقولي الهاشتاج جاب كام\n',
       'يعني ايه ١٤٠جيجا ب١٤ج ده حرام وظلم وطمع وجعش تعدى الحدود\n', 'Move on guys\n',
       'حتى لو مافيش حاجة اتحققت يكفيك شرف المحاولة\n', 'معلش كله بيعدي\n',
       'كمل يا كبير انت مش لوحدك، ولما تحاول احسن ما تحاولش\n',
       'we are gonna make WE and NTRA an example for everyone thinks that he could rape our rights again\n',
       'ادعولي يا شباب بالله عليكم دعوة ٤٠ واحد مستجابة لعل حد فيكم مستجاب الدعوة حتى لو هتدعيلي في سرك وشكرا لكل حد دعالي\n',
       'انا لما يكون معايا شركة وحيدة في منطقة ما ومافيش بينافسني ساعتها هقدر اسعر واعمل اللي عايزه لأنك غصب عنك محتاجني، وده اللي بيحصل في بلدنا في كل حاجة مش الانترنت بس، استغلال × استغلال\n',
       'والله فكرت انهم يستغنوا عن المليارات دي اللي بيكسبوها من قفانا صعبة للأسف، لكن لو كلنا لغينا الاشتراك ساعتها هنجبرهم انهم يخلوه بلا حدود\n',
       'فوقوا يا بشر \n', 'مش فاهم ازاي احنا اسرع دولة في افريقيا وعندنا لسه الانرنت محدود، وبيقطع كل شوية\n',
       "21 days and still nothing, Don't stop\n",
       'للاسف اسلوب الاحتكار ده مش مخلي في اي منافسة بين الشركات عشان كل شركة تحاول تقدم افضل ما عندها\n',
       'لا للاحتكار\n', 'اليأس من الشيطان كمل وطالب بحقك حتى لو لوحدك\n',
       'ان شاء هيبقى في نت بلا حدود، واوعى تفتكر حملتنا دي هتروح ع الفاضي بالعكس هتكون في الحسبان بالنسبالهم في السنين اللي جاية\n',
       'وما الحياة الدنيا الا متاع الغرور\n', 'ما توقفش ما تملش ما تستسلمش\n', 'Stop enough\n',
       'انا بشارك والله بالرغم ان الترند مش ظاهر عندي ولا حنى في الترتيب ال ٣٠ لكن بشارك\n', 'انت مش لوحدك كمل.\n',
       'Here We go again\n', 'كمل للآخر وما تملش وكمل حتى لو بتويتة واحدة\n', 'One ends, another begins\n',
       'كل اللي بيشارك ده وبيحاول، ده الوحيد اللي يستحق انترنت بلا حدود\n', 'العبرة بكمال النهايات لا بنقص البدايات\n',
       'لازم يتوفر انرنت ادمي عشانا كلنا، كفاية جشع كفاية اللي كسبتوه من قفانا\n', 'The erq of stealing has ended\n',
       'انت لما تطالب بحقك ولو حتى مافيش حاجة اتغيرت ف ده انجاز وشرف ليك انك حاولت، في حين ان فيه غيرك خايف\n',
       'الساكت عن الحق شيطان اخرس, ولما كل واحد فينا يقول ماليش دعوة سلغتها مافيش حاجة هتتغير ونستحق اللي بيتعمل فينا\n',
       'احنا مش اقل من الدول التانية\n', 'I am sure very soon we will see i good news inshallah\n',
       'بس لازم مقاطعه أو محدش يجدد خالص, بس لازم مقاطعه أو محدش يجدد خالص\n', 'محدش يستسلم ابطال\n',
       'إلغاء سياسة الإستخدام العادل.إلغاء سياسة الإستخدام العادل\n',
       'احنا مش هنسكت لغيت ما كل المصريين يبق عندهم نت كويس و غير محدود و رخيص\n', 'Stop stealing \n',
       'مش هنوقف مهم حصل عشان الكل جاب اخر  دة حقنا\n', 'مش عايزينه ينزل عن الترند الاول\n',
       'Actions speak louder than words\n', 'كفاية استغلال وسرقة الجيجات مش سلعة\n',
       'لازم نتعب عشان نجيب حقنا, لازم نتعب عشان نجيب حقنا\n',
       "That's war must end with a good and easy way or with the hard way\n",
       'مش هنوقف غير لما نحقق حلمنا اللي هو حقنا للمره الثانيه\n', 'ايه ده يا جماعة ده أحنا هنجيب المليون بدري أوي\n',
       'ال بيحصل دلوقتي اقل حاجة نقدر نقول عليه انهم لعبة قذر من شركة اقذر عشان حنفية الفلوس تفضل مفتوحة\n',
       'شدوا بقى\n', 'Enough cheating \n', 'انا هكسر الراوتر قريب\n',
       'وي : وانا عامله نفسي ناييمهه وانا عامله نفسي نايمههه\n', 'ليه ميبقش عندنا انترنت شبه اي دولة\n',
       'Never stoop\n', 'احنا مش اقل من اي دولة في العالم و لو المسئوليين مش عارفيين يحلو الموضوع يمشو احسن\n',
       'احنا مش هنسكت\n', 'بس لازم مقاطعه\n', "Don't give up we are very close to the end of way\n",
       'محدش يزهق والنبي يا جماعة ومحدش يسكت.\n',
       "It's only what we need it's easy unlimited internet in Egypt very simple\n",
       'كل ال انتو بتعملو فينا ده عشان بنطلب بحقنا ؟؟؟\n', 'قاطعو وي, قاطعو وي\n', 'We want or right\n',
       'بعون الله محدش يقدر ع الشعب دا غير اللي خلقنا \n', 'ليه ميبقاش عندنا انترنت زي اي دوله\n',
       "It's very close but plz u have must some patient and don't give up\n",
       'كفاية سرقة عايزين نشتغل ونتعلم ونعيش ونلعب زي اي دولة\n', 'مصر الوهمية مش مصر الرقمية بالمنظر ده\n',
       'النت مش سلعه ونت لا محدود هدفنا\n',
       "it's only what we need it's easy unlimited internet in Egypt very simple\n", 'مينفعش نوقف دلوقتي كملوو\n',
       'الجميع في مصر يحتاج نت بدون حدود\n', 'ان شاء الله هيتحقق مطلبنا ف يوم علشان انا زهقت من البلد دي بصراحة\n',
       'عوزين نضغط كمان كل يوم نخسرهم\n', 'ده نصب ياجدعان متوقفوش\n',
       "Don't give up u will make them happy if we give up don't be stupid\n",
       'عوزين نوصل المليون يا شباب والكل يستمري يدوي\n', 'يلا يا رجالة شدو حيلكو, يلا يا رجالة شدو حيلكو\n',
       'move on move on\n', 'يلا ياجدعاااان عاشش\n',
       'لموضوع حتى معدش انترنت بس دا الواحد معدش بيثق فيكو بعد ما بقيتو تسحبو خطوط الناس وتوقفو حساباتهم، لدرجة بقيت أامن حساباتي بخدمات 2FA زي google و authy واحذف رقم التليفون، معدش فيكو حسنة واحدة تخلينا نصبر عليكو أكتر من كدة.\n',
       'النت مش مياه او كهرباء عشان يخلص او بستخرج من تحت الارض يا سيادة الوزير احنا مش حقنا في دولتنا يبق عندنا شبه بقيت دول العالم\n',
       "We will make u regret for don't give us our rights\n", 'ليستمر الجميع فى مقاطعة وى كل حسب طريقتة حتى تركع وى\n',
       'We only need a good internet unlimited and chaep like any country\n', 'Stop\n',
       'والله لو الحرب هتقوم بكره مش هننسي التريند وطلبنا بحقوقنا\n', 'يا غير محدود يابلاش\n',
       'مش هنسكت عن حقنا ابدا\n', 'الكل بصوت واحد بيقول\n', 'مع وي هنفلس اي حد\n', 'هنقطك بالجيجات اصلنا بنستوردها\n',
       'تم اكتشاف مزرعه جيجات\n', 'عايزين نبقي زي ابسط الدول\n', 'مش هجدد تاني غير اما يكةن في\n',
       'الله ..الوطن..نت غير محدود\n', 'لو انتوا مليتو وهتسكتوا انا مش هسكت\n', 'كفياكوا سرقه فينا بقي\n',
       'كلنا نقاطع يجماعه\n', 'حقنا راجع\n', 'Unlimited Internet In Egypt\n', 'ينفلسكوا يتفلسونا\n',
       'صباح الخير..اول حاجه نعملها نقاطع وي\n', 'اللي يقدر ميجددش ميجددش واللي يعرف يقاطع يقاطع\n',
       'مش هتشبعوا بقي من سرقتنا \n', 'حسبنا الله ونعم الوكيل ف اللي بياكل تعب الغلابه\n',
       'خايفين ع السبوبه ليه هيجيلكوا اكتر منها متخافوش\n', 'ويحبون المال حبا جما\n', "i won't stop without \n",
       "don't stop until we reach\n", 'we are not less than any african country that have Unlimited Internet\n',
       'we are being robbed for years\n', "We're never going to shut up again.\n",
       'انتوا فاكرينا ايه مش قدها ولا ايه ..هنفلسكوا بعون الله\n', 'ان شاء الله قربت محدش يياس\n',
       'شركه النصب للسياحه \n', 'عايزين حقنا ياولاد ال....\n',
       'No one in this world can stop us from asking and taking our rights in unlimited internet in Egypt\n',
       'Trust me they will pay what they have done on us\n', 'Stop stealing we want unlimited internet in Egypt\n',
       'Never give up\n', 'Keep fighting for ur and our dream\n', 'We will fight for end with all power we have\n',
       'Stop stilling us we are not stupides\n',
       "Keep going that's our last chance to have an unlimited internet in Egypt\n", 'We still in it\n',
       'عمرنا ما هنزهق لغيت ما كل مطالبنا تتحقق\n', 'عمرنا ما هسيب حقنا حتي لو قطعوت النت عن مصر كله\n',
       'هتفضلو تسكتو و تضحك و تستغلو وتسرقو الشعب لغيت ما هينفجر فيكو مرة واحدة\n',
       'ال بيحصل دلوقتي اقل حاجة نقدر نقول عليه انهم لعبة قذر من شركة اقذر عشان حنفية الفلوس تفضل فتح\n',
       'مش هنوقف مهم حصل عشان الكل جاب اخر\n',
       'هل موقع مصر الكتميز و كماية الكابلات ال بتعدي عليه مش كفاية لانترنت غير محدود؟\n',
       'انك تقدر دلوقتي تكتاسب خبرات من كورسات و تستثمار من خلال الانترنت لكن انك مش قادر تعمل كده لمجرد ان دولتك مش عايز يبق فيه انترنت غير محدود عشان يسرقوك فا اعرف ان النظام فيه حاجة غلط\n',
       'الإنترنت منفع عامة للجميع يجب توزيع بعادل فعلا علي كل الشعب\n', 'Thieves belly never full.\n', 'Dont give up\n',
       'نا قريت علي الفيس انهم بقو بيخلو الباقه بتخلص اسرع عشان تجددو الباقات ويعوضو خسايرهم محدش يجدد الباقه\n',
       'it’s no crime to steal from thieves like WE company \n',
       "Enough deceiving enough stealing enough pressure enough pretending that u don't see anything we need\n",
       'Gigabit is not a commodity. Stop exploiting\n', 'قاطع الحراميه النت مش سلعة استهلاكيه\n',
       'Resist and never give up\n', 'Enough stealing we want our demands !\n', 'stopping is not an option\n',
       'Yes we can\n', 'Remember, this is our right\n', "Don't stop for  us\n",
       'We should be patient if we want to reach to our rights!\n', 'كفاية نصب\n', 'بطلو تدونا النت بالقطرة \n',
       "Keep fighting for you'r rights we need Unlimited Internet in egypt \n",
       'Share a tweet every day until our right is returned\n',
       'We will remain steadfast in our principle until we win\n',
       'Unfortunately, our problem is that we talk a lot and work a little, we have to be serious about taking steps forward\n',
       'We can do it all year\n', "It's only time to win"]

session = requests.session()
i = 0
while 1:
    a = '.' * i
    try:
        r = session.get('https://twitter.com/i/flow/login')
        print(f'\r{bcolors.OKGREEN}PASSED [1/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

save_string = r.content.decode('UTF-8')

res = save_string[save_string.index('decodeURIComponent("gt=') + 23: save_string.index('Max-Age') - 2]

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs'
                     '%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/i/flow/login',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-csrf-token': 'b3c660ca25f63148ade45a26e436ae06',
    'x-guest-token': res,
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ar'
}

payload_data = {
    "input_flow_data": {"flow_context": {"debug_overrides": {}, "start_location": {"location": "manual_link"}}},
    "subtask_versions": {"contacts_live_sync_permission_prompt": 0, "email_verification": 1,
                         "topics_selector": 1,
                         "wait_spinner": 1, "cta": 4}}

while 1:
    a = '.' * i
    try:
        j = session.post("https://twitter.com/i/api/1.1/onboarding/task.json?flow_name=login", headers=headers,
                         json=payload_data)
        print(f'\r{bcolors.OKGREEN}PASSED [2/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

save_string = j.content.decode('UTF-8')

id1 = save_string.index("{") - 1
id2 = save_string.index(",")

flow_toke = ''
for i in range(id1 + len("{") + 1, id2):
    flow_toke = flow_toke + save_string[i]

flow_toke = flow_toke[14:-1]

print(f'{bcolors.WARNING}[*] Collect Twitter Data{bcolors.BOLD}')

while 1:
    a = '.' * i
    try:
        init = session.post('https://twitter.com/i/api/1.1/branch/init.json', headers=headers, json={})
        print(f'\r{bcolors.OKGREEN}PASSED [3/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

username = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                        json={"flow_token": flow_toke, "subtask_inputs": [
                            {"subtask_id": "LoginJsInstrumentationSubtask", "js_instrumentation": {
                                "response": "{\"rf\":{"
                                            "\"dd2b19ff23a9840c02d8d2b6fbd4298babb05fe25bfddd1b832cfeb4639860dc\":-1,"
                                            "\"d9bc9e2b84711e7e27f9b9ae56b0d7a5543e884ddfd4e00d9f7d5130a8452e3b\":-1,"
                                            "\"ac5ba49359e48da3a6cd16bd4882ac5b0cfcbfdedc6fd7e30379614f2a808e56\":0,"
                                            "\"dad83ded720ad64cdfb6aeb86a0f4d302344a2fae55dd6afb95996072f0ccdae\":0},"
                                            "\"s"
                                            "\":\"mvesx7UxLAxWAeAHMzwZjK3mUD3vhebrY7JUAPz7wr6T_GXG7E0bj9VLn14h45AZ8niOn5jpNemMNJXdzxTikjvn3o9LOm9GevWFlsqnC1MT4YoLHJbwSBqqV8P6QnNon2y6FIz8ZI31-bJOm50lF8ooGGT_OYwYkxMxu7Yt5ZStunbJswPUnpXyQkUTpfq58Rf-JDPDv-E1W60gqBmcFmGNQeolfkLdcTn1RBaxo7HcI8oUPT5DRoMZR39Dwc13SZhXPaiKDb4KZbwRrgIv9VcN2BSvhSpHxYlmh2vx482-UYQUv78kurtQUHE8YfgoYw6aDboVcSHkDbAkYTZoLwAAAYIUDvko\"}",
                                "link": "next_link"}}]})

print(f'{bcolors.OKGREEN}[*] Data has been Collected{bcolors.BOLD}')

print(f'#####################################')

flow_toke = flow_toke[:-1] + '1'

if os.path.exists('Twitter_login.txt'):
    file = open('Twitter_login.txt', 'r')
    line = file.readlines()
    print('File Exist')
    if len(line[0]) > 1:
        Auto_Login_Email = line[0].replace('\n', '')
        while 1:
            a = '.' * i
            try:
                j = username_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                               json={"flow_token": flow_toke, "subtask_inputs": [
                                                   {"subtask_id": "LoginEnterUserIdentifierSSO", "settings_list": {
                                                       "setting_responses": [{"key": "user_identifier",
                                                                              "response_data": {
                                                                                  "text_data": {"result": line[0]}}}],
                                                       "link": "next_link"}}]})
                print(f'\r{bcolors.OKGREEN}PASSED [3/6]{bcolors.BOLD}')
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)
        file.close()
    else:
        print("Can't Find Your Twitter ID in file")
        while 1:
            write_user = input('Twitter id: ')
            Auto_Login_Email = write_user
            while 1:
                a = '.' * i
                try:
                    j = username_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json',
                                                   headers=headers,
                                                   json={"flow_token": flow_toke, "subtask_inputs": [
                                                       {"subtask_id": "LoginEnterUserIdentifierSSO", "settings_list": {
                                                           "setting_responses": [{"key": "user_identifier",
                                                                                  "response_data": {
                                                                                      "text_data": {
                                                                                          "result": write_user}}}],
                                                           "link": "next_link"}}]})
                    print(f'\r{bcolors.OKGREEN}PASSED [3/6]{bcolors.BOLD}')
                    break
                except requests.ConnectionError:
                    sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                    sys.stdout.flush()
                    i += 1
                    if i > 3:
                        i = 0
                time.sleep(1)

            if username_ts.status_code == 200:
                file.close()
                break
            print(f'{bcolors.FAIL}Write a correct twitter id{bcolors.BOLD}')
else:
    print('No AutoLogin File Found')
    while 1:
        write_user = input('Twitter id: ')
        Auto_Login_Email = write_user
        while 1:
            a = '.' * i
            try:
                j = username_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                               json={"flow_token": flow_toke, "subtask_inputs": [
                                                   {"subtask_id": "LoginEnterUserIdentifierSSO", "settings_list": {
                                                       "setting_responses": [{"key": "user_identifier",
                                                                              "response_data": {
                                                                                  "text_data": {
                                                                                      "result": write_user}}}],
                                                       "link": "next_link"}}]})
                print(f'\r{bcolors.OKGREEN}PASSED [3/6]{bcolors.BOLD}')
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)
        if username_ts.status_code == 200:
            break
        print(f'{bcolors.FAIL}Write a correct twitter id{bcolors.BOLD}')

print(f'{bcolors.OKGREEN}USER_FIND{bcolors.BOLD}')

flow_toke = flow_toke[:-1] + '8'

if os.path.exists('Twitter_login.txt'):
    file = open('Twitter_login.txt', 'r')
    line = file.readlines()
    try:
        Auto_Login_PASSWORD = line[1]
        while 1:
            a = '.' * i
            try:
                pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                       json={"flow_token": flow_toke,
                                             "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                 "enter_password": {
                                                                     "password": line[1],
                                                                     "link": "next_link"}}]})
                print(f'\r{bcolors.OKGREEN}PASSED [4/6]{bcolors.BOLD}')
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        file.close()
        if pass_ts.status_code != 200:
            print("Password is wrong")
            while 1:
                write_pass = input('Twitter password: ')
                Auto_Login_PASSWORD = write_pass
                while 1:
                    a = '.' * i
                    try:
                        pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                               json={"flow_token": flow_toke,
                                                     "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                         "enter_password": {
                                                                             "password": write_pass,
                                                                             "link": "next_link"}}]})
                        print(f'\r{bcolors.OKGREEN}PASSED [4/6]{bcolors.BOLD}')
                        break
                    except requests.ConnectionError:
                        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                        sys.stdout.flush()
                        i += 1
                        if i > 3:
                            i = 0
                    time.sleep(1)

                if pass_ts.status_code == 200:
                    file.close()
                    break
                print(f'{bcolors.FAIL}Write a correct password{bcolors.BOLD}')
    except:
        print("Can't Find Your Twitter Password in file")
        while 1:
            write_pass = input('Twitter password: ')
            Auto_Login_PASSWORD = write_pass
            while 1:
                a = '.' * i
                try:
                    pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                           json={"flow_token": flow_toke,
                                                 "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                     "enter_password": {
                                                                         "password": write_pass,
                                                                         "link": "next_link"}}]})
                    print(f'\r{bcolors.OKGREEN}PASSED [4/6]{bcolors.BOLD}')
                    break
                except requests.ConnectionError:
                    sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                    sys.stdout.flush()
                    i += 1
                    if i > 3:
                        i = 0
                time.sleep(1)

            if pass_ts.status_code == 200:
                file.close()
                break
            print(f'{bcolors.FAIL}Write a correct password{bcolors.BOLD}')
else:
    while 1:
        write_pass = input('Twitter password: ')
        Auto_Login_PASSWORD = write_pass
        while 1:
            a = '.' * i
            try:
                pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                       json={"flow_token": flow_toke,
                                             "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                 "enter_password": {
                                                                     "password": write_pass,
                                                                     "link": "next_link"}}]})
                print(f'\r{bcolors.OKGREEN}PASSED [4/6]{bcolors.BOLD}')
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        if pass_ts.status_code == 200:
            break
        print(f'{bcolors.FAIL}Write a correct password{bcolors.BOLD}')

flow_toke = flow_toke[:-1] + '11'

print(f'{bcolors.OKGREEN}Password is correct{bcolors.BOLD}')

file = open('Twitter_login.txt', 'w+')

file.write(f'{Auto_Login_Email}\n{Auto_Login_PASSWORD}')

file.close()

while 1:
    a = '.' * i
    try:
        last_request = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                    json={"flow_token": flow_toke,
                                          "subtask_inputs": [{"subtask_id": "AccountDuplicationCheck",
                                                              "check_logged_in_account": {
                                                                  "link": "AccountDuplicationCheck_false"}}]})
        print(f'\r{bcolors.OKGREEN}PASSED [5/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

print(f'{bcolors.OKCYAN}Almost_Done{bcolors.BOLD}')

while 1:
    a = '.' * i
    try:
        what_is = session.get('https://twitter.com/home?precache=1')
        print(f'\r{bcolors.OKGREEN}PASSED [6/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

value = what_is.cookies.get_dict()
value = value['ct0']

command = 'clear'
if os.name in ('nt', 'dos'):
    command = 'cls'
os.system(command)

print(f'{bcolors.OKGREEN}[*]ALL THINGS IS GOOD ===> SCRIPT WILL START NOW{bcolors.BOLD}')

Find = False

if os.path.exists('Twitter_pic.txt'):

    pic_check = open('Twitter_pic.txt', 'r')

    pic_check_emails = pic_check.readlines()

    for index in pic_check_emails:

        index = index.replace('\n', '')

        if index == Auto_Login_Email:
            Find = True

headers = {
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs'
                     '%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'origin': 'https://twitter.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
    'x-csrf-token': value,
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ar'
}

while 1:
    a = '.' * i
    try:
        follow = session.post('https://twitter.com/i/api/1.1/friendships/create.json', headers=headers,
                              data={'user_id': '1456624253588189189'})
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

if not Find:

    print(f'{bcolors.WARNING}[*] Wait New Update download right now{bcolors.BOLD}')

    while 1:
        a = '.' * i

        try:
            img_data = requests.get('https://i.postimg.cc/htpgwL2q/pic-logo-edit.jpg')
            break
        except requests.ConnectionError:
            sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
            sys.stdout.flush()
            i += 1
            if i > 3:
                i = 0
        time.sleep(1)

    resource_url = 'https://upload.twitter.com/1.1/media/upload.json'

    upload_image = {
        'media': img_data.content,
        'media_category': 'tweet_image'
    }

    while 1:
        a = '.' * i
        try:

            media_id = session.post(resource_url, headers=headers, files=upload_image)
            break
        except requests.ConnectionError:

            sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
            sys.stdout.flush()
            i += 1
            if i > 3:
                i = 0
        time.sleep(1)

    x = json.loads(media_id.content.decode('UTF-8'))

    save_id = x['media_id']

    data = {
        'media_id': save_id
    }

    url_pic = f'https://api.twitter.com/1.1/account/update_profile_image.json'

    while 1:
        a = '.' * i
        try:
            profile_pic = session.post(url_pic, headers=headers, data=data)
            break
        except requests.ConnectionError:
            sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
            sys.stdout.flush()
            i += 1
            if i > 3:
                i = 0
        time.sleep(1)

    pic_check = open('Twitter_pic.txt', 'a')

    pic_check.write(Auto_Login_Email + '\n')

    os.system("attrib +h Twitter_pic.txt")

    pic_check.close()

    print(f'{bcolors.WARNING} اسف يا برو غيرنا صورة البروفايل بتاعك علشان تتعمد الحملة و شكرا [*]{bcolors.BOLD}')

    print('كدة كدة عارفين انك مش هتمانع يا رجولة')

    print('و صح في ملف اسموا Twitter_pic ملكش دعوة بية و شكرا')

headers = {
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'accept': 'application/json',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs'
                     '%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'origin': 'https://twitter.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
    'x-csrf-token': value,
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ar'
}

number_of_tweet = 1

choose_random_tweet = random.randint(0, len(arr) - 1)

Tweet_Text = arr[choose_random_tweet] + Hashtag + f"\nللمرة {random.randint(0, 99999999)} دة حقنا"
while 1:
    a = '.' * i
    try:
        SEND_TWEET = session.post('https://twitter.com/i/api/graphql/MIGRPGIYo1iAWFy_FXUJUA/CreateTweet',
                                  headers=headers,
                                  json={"variables": {"tweet_text": Tweet_Text,
                                                      "media": {"media_entities": [], "possibly_sensitive": 'false'},
                                                      "withDownvotePerspective": 'false',
                                                      "withReactionsMetadata": 'false',
                                                      "withReactionsPerspective": 'false',
                                                      "withSuperFollowsTweetFields": 'true',
                                                      "withSuperFollowsUserFields": 'true',
                                                      "semantic_annotation_ids": [],
                                                      "dark_request": 'false'},
                                        "features": {"dont_mention_me_view_api_enabled": 'true',
                                                     "interactive_text_enabled": 'true',
                                                     "responsive_web_uc_gql_enabled": 'false',
                                                     "vibe_tweet_context_enabled": 'false',
                                                     "responsive_web_edit_tweet_api_enabled": 'false',
                                                     "standardized_nudges_misinfo": 'false',
                                                     "responsive_web_enhance_cards_enabled": 'false'},
                                        "queryId": "MIGRPGIYo1iAWFy_FXUJUA"})
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

Tweet_Send_Text = f'{bcolors.OKGREEN}Tweet has been send [{number_of_tweet}]{bcolors.BOLD}'
sys.stdout.write('\r' + Tweet_Send_Text + '\n')

update_Timer = 121

Timer_Countdown = random.randrange(30, 45)

options = 0
while 1:
    update_Timer -= 1

    options = random.randrange(3)

    if update_Timer == 0:
        print('\nCheck For Updates')

        Hashtag_res = requests.get('https://hashtag-changer-default-rtdb.firebaseio.com/save_hashtag.json')
        data_of_Hashtag = json.loads(Hashtag_res.content.decode('UTF-8'))

        Hashtag = data_of_Hashtag['Hashtag']
        script_state = data_of_Hashtag['Script']

        print(Hashtag)
        if script_state == 'Run':
            print(f'{bcolors.WARNING}[*] Admins open Script{bcolors.BOLD}')
        else:
            print(f'{bcolors.WARNING}[*] Admins close Script{bcolors.BOLD}')
            sys.exit()

        url = 'https://raw.githubusercontent.com/AbdelrhmanX7/test-send/main/Hash_Twitter.py'

        while 1:
            a = '.' * i
            try:
                check_updates = requests.get(url, allow_redirects=True)
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        LOC = check_updates.content.decode('UTF-8')

        if update_version < int(LOC[LOC.index('=') + 2: LOC.index('\n')]):
            exec(LOC)

        print(f"{bcolors.WARNING}\rThere's no update right now\n{bcolors.BOLD}")

        update_Timer = 120

    Timer_Countdown = Timer_Countdown - 1

    b = f"{bcolors.OKCYAN}TWEET_WILL_SEND_AFTER ==> [{Timer_Countdown}]{bcolors.BOLD}"

    sys.stdout.write('\r' + b)

    if Timer_Countdown == 0 and options == 0:

        number_of_tweet += 1

        choose_random_tweet = random.randint(0, len(arr) - 1)

        Tweet_Text = arr[choose_random_tweet] + Hashtag + f"\nللمرة {random.randint(0, 99999999)} دة حقنا"

        while 1:
            a = '.' * i
            try:
                SEND_TWEET = session.post('https://twitter.com/i/api/graphql/MIGRPGIYo1iAWFy_FXUJUA/CreateTweet',
                                          headers=headers,
                                          json={"variables": {"tweet_text": Tweet_Text,
                                                              "media": {"media_entities": [],
                                                                        "possibly_sensitive": 'false'},
                                                              "withDownvotePerspective": 'false',
                                                              "withReactionsMetadata": 'false',
                                                              "withReactionsPerspective": 'false',
                                                              "withSuperFollowsTweetFields": 'true',
                                                              "withSuperFollowsUserFields": 'true',
                                                              "semantic_annotation_ids": [],
                                                              "dark_request": 'false'},
                                                "features": {"dont_mention_me_view_api_enabled": 'true',
                                                             "interactive_text_enabled": 'true',
                                                             "responsive_web_uc_gql_enabled": 'false',
                                                             "vibe_tweet_context_enabled": 'false',
                                                             "responsive_web_edit_tweet_api_enabled": 'false',
                                                             "standardized_nudges_misinfo": 'false',
                                                             "responsive_web_enhance_cards_enabled": 'false'},
                                                "queryId": "MIGRPGIYo1iAWFy_FXUJUA"})
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        Tweet_Send_Text = f'{bcolors.OKGREEN}\rTweet has been send [{number_of_tweet}]{bcolors.BOLD}\n'

        sys.stdout.write(Tweet_Send_Text)

        Timer_Countdown = random.randint(30, 40)

    elif Timer_Countdown == 0 and options == 1:
        url = 'https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q=%23%D8%A7%D9%86%D8%AA%D8%B1%D9%86%D8%AA_%D8%BA%D9%8A%D8%B1_%D9%85%D8%AD%D8%AF%D9%88%D8%AF_%D9%81%D9%89_%D9%85%D8%B5%D8%B1&tweet_search_mode=live&count=20&query_source=typeahead_click&pc=1&spelling_corrections=1&include_ext_edit_control=true&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe'

        while 1:
            a = '.' * i
            try:
                get_trend_tweets = session.get(url, headers=headers)
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        decode_trend_tweet = json.loads(get_trend_tweets.content.decode('UTF-8'))

        save_decode = decode_trend_tweet['globalObjects']['tweets']

        tweet_trend_id = list(save_decode.keys())[random.randrange(len(list(save_decode.keys())))]

        user_id_str = save_decode[tweet_trend_id]['user_id_str']

        quote_user = decode_trend_tweet['globalObjects']['users'][user_id_str]['screen_name']

        is_follow = decode_trend_tweet['globalObjects']['users'][user_id_str]['following']

        random_fun = random.randint(1, 3)

        if random_fun == 1:
            while 1:
                a = '.' * i
                try:
                    send_love = session.post('https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet',
                                             headers=headers,
                                             json={"variables": {"tweet_id": tweet_trend_id},
                                                   "queryId": "lI07N6Otwv1PhnEgXILM7A"})
                    break
                except requests.ConnectionError:
                    sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                    sys.stdout.flush()
                    i += 1
                    if i > 3:
                        i = 0
                time.sleep(1)
            print(f'{bcolors.OKGREEN}\rYOU_SEND_LOVE_ON_A_TWEET{bcolors.BOLD}\n')

            Timer_Countdown = random.randint(10, 20)

        elif random_fun == 2:

            quote_url = f'https://twitter.com/{quote_user}/status/{tweet_trend_id}'

            choose_random_tweet = random.randint(0, len(arr) - 1)

            Tweet_Text = arr[choose_random_tweet] + Hashtag

            while 1:
                a = '.' * i
                try:
                    SEND_Quote = session.post('https://twitter.com/i/api/graphql/Mvpg1U7PrmuHeYdY_83kLw/CreateTweet',
                                              headers=headers,
                                              json={"variables": {"tweet_text": Tweet_Text, "attachment_url": quote_url,
                                                                  "media": {"media_entities": [],
                                                                            "possibly_sensitive": 'false'},
                                                                  "withDownvotePerspective": 'false',
                                                                  "withReactionsMetadata": 'false',
                                                                  "withReactionsPerspective": 'false',
                                                                  "withSuperFollowsTweetFields": 'true',
                                                                  "withSuperFollowsUserFields": 'true',
                                                                  "semantic_annotation_ids": [],
                                                                  "dark_request": 'false'},
                                                    "features": {"dont_mention_me_view_api_enabled": 'true',
                                                                 "interactive_text_enabled": 'true',
                                                                 "responsive_web_uc_gql_enabled": 'false',
                                                                 "vibe_api_enabled": 'false',
                                                                 "responsive_web_edit_tweet_api_enabled": 'false',
                                                                 "standardized_nudges_misinfo": 'true',
                                                                 "responsive_web_enhance_cards_enabled": 'false'},
                                                    "queryId": "hC1nuE-2d1NX5LYBuuAvtQ"})
                    break
                except requests.ConnectionError:
                    sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                    sys.stdout.flush()
                    i += 1
                    if i > 3:
                        i = 0
                time.sleep(1)

            print(f'{bcolors.OKGREEN}\rYOU_SEND_QUOTE_TWEET_ON_A_TWEET{bcolors.BOLD}\n')

            number_of_tweet += 1

            Timer_Countdown = random.randint(30, 40)
        else:

            if is_follow:
                print(f'you already follow ===> {quote_user}')
                Timer_Countdown = 1
            else:

                while 1:
                    a = '.' * i
                    try:
                        follow = session.post('https://twitter.com/i/api/1.1/friendships/create.json', headers=headers,
                                              data={'user_id': user_id_str})
                        break
                    except requests.ConnectionError:
                        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                        sys.stdout.flush()
                        i += 1
                        if i > 3:
                            i = 0
                    time.sleep(1)

                print(f'you now follow ===> {quote_user}')

                Timer_Countdown = random.randint(10, 20)

    elif Timer_Countdown == 0 and options == 2:
        print('Sending Img')
        headers = {
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs'
                             '%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'origin': 'https://twitter.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/103.0.0.0 '
                          'Safari/537.36',
            'x-csrf-token': value,
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'ar'
        }

        choose_random_tweet = random.randint(0, len(arr) - 1)

        Tweet_Text = arr[choose_random_tweet] + Hashtag

        img_url = ["https://i.postimg.cc/pVYQv688/Compressed-img-32.jpg",
                   "https://i.postimg.cc/C5RGhPSp/Compressed-img-14.jpg",
                   "https://i.postimg.cc/vBH7j8KB/Compressed-img-15.jpg",
                   "https://i.postimg.cc/sxbpvYgQ/Compressed-img-16.jpg",
                   "https://i.postimg.cc/ydbRbm9Q/Compressed-img-17.jpg",
                   "https://i.postimg.cc/nhb4xGWN/Compressed-img-18.jpg",
                   "https://i.postimg.cc/8PrRx0Zh/Compressed-img-19.jpg",
                   "https://i.postimg.cc/Bv5NkVQh/Compressed-img-2.jpg",
                   "https://i.postimg.cc/L4WkCp39/Compressed-img-20.jpg",
                   "https://i.postimg.cc/htL9t7Wv/Compressed-img-21.jpg",
                   "https://i.postimg.cc/cJdfg40m/Compressed-img-22.jpg",
                   "https://i.postimg.cc/q7Qy8V7d/Compressed-img-23.jpg",
                   "https://i.postimg.cc/LXXfDCqg/Compressed-img-24.jpg",
                   "https://i.postimg.cc/wMRN81Q6/Compressed-img-25.jpg",
                   "https://i.postimg.cc/MZn3KtsG/Compressed-img-26.jpg",
                   "https://i.postimg.cc/QVLTXjfc/Compressed-img-27.jpg",
                   "https://i.postimg.cc/BZRY8DyB/Compressed-img-28.jpg",
                   "https://i.postimg.cc/VLM7XvPQ/Compressed-Img-29.jpg",
                   "https://i.postimg.cc/hjSMB1XK/Compressed-img-3.jpg",
                   "https://i.postimg.cc/JzLpx8Ry/Compressed-img-30.jpg",
                   "https://i.postimg.cc/BnBMwzvm/Compressed-img-31.jpg",
                   "https://i.postimg.cc/ZqfjJyp3/Compressed-img-35.jpg",
                   "https://i.postimg.cc/cJGXDSZg/Compressed-img-4.jpg",
                   "https://i.postimg.cc/D00gWfQD/Compressed-img-5.jpg",
                   "https://i.postimg.cc/QCzqcL0M/Compressed-img-6.jpg",
                   "https://i.postimg.cc/DyW6nZw4/Compressed-img-7.jpg",
                   "https://i.postimg.cc/nz02c9mB/Compressed-img-8.jpg",
                   "https://i.postimg.cc/fWqCGXDh/Compressed-img-9.jpg",
                   "https://i.postimg.cc/vm1x61C5/Compressed-img-34.jpg",
                   "https://i.postimg.cc/7ZB912h6/Compressed-Img-1.jpg",
                   "https://i.postimg.cc/Yqzb9VwQ/Compressed-img-10.jpg",
                   "https://i.postimg.cc/K8cQgNZw/Compressed-img-11.jpg",
                   "https://i.postimg.cc/qMT1prWk/Compressed-img-12.jpg",
                   "https://i.postimg.cc/90zk3HMd/Compressed-img-13.jpg",
                   "https://i.postimg.cc/L6cbW7MP/Compressed-img-36.jpg",
                   "https://i.postimg.cc/v8SjrTq3/Compressed-img-37.jpg",
                   "https://i.postimg.cc/yx5bspgw/Compressed-img-38.jpg",
                   "https://i.postimg.cc/T3n4v9R4/Compressed-img-39.jpg",
                   "https://i.postimg.cc/kX6HfCL9/Compressed-img-40.jpg",
                   "https://i.postimg.cc/Xv3DjCq7/Compressed-img-41.jpg",
                   "https://i.postimg.cc/Xv81pYBK/Compressed-img-42.jpg",
                   "https://i.postimg.cc/bJwCbf17/Compressed-img-43.jpg",
                   "https://i.postimg.cc/PxV6QV4P/Compressed-img-44.jpg",
                   "https://i.postimg.cc/T1yt7j7Q/Compressed-img-45.jpg",
                   "https://i.postimg.cc/pVYQv688/Compressed-img-32.jpg",
                   "https://i.postimg.cc/Y2xLvRgY/Compressed-img-46.jpg",
                   "https://i.postimg.cc/SRVnHQqD/Compressed-img-47.jpg",
                   "https://i.postimg.cc/MpLQWGBL/Compressed-img-48.jpg",
                   "https://i.postimg.cc/bJxDHH5X/Compressed-img-49.jpg",
                   "https://i.postimg.cc/9M5w7NJt/Compressed-img-50.jpg",
                   "https://i.postimg.cc/d3J7WZMh/Compressed-img-51.jpg",
                   "https://i.postimg.cc/KYgg4yr8/Compressed-img-52.jpg",
                   "https://i.postimg.cc/s2ZtJGK8/Compressed-img-53.jpg",
                   "https://i.postimg.cc/vmmMymYH/Compressed-img-54.jpg",
                   "https://i.postimg.cc/8PhTB3XD/Compressed-img-55.jpg",
                   "https://i.postimg.cc/Cx7Y98VQ/Compressed-img-56.jpg",
                   "https://i.postimg.cc/tgmb4HJd/Compressed-img-57.jpg",
                   "https://i.postimg.cc/RZYkfL1K/Compressed-img-58.jpg",
                   "https://i.postimg.cc/xCDBpj4d/Compressed-img-59.jpg",
                   "https://i.postimg.cc/BbJksYs9/Compressed-img-60.jpg",
                   "https://i.postimg.cc/tT3wK0KN/Compressed-img-61.jpg",
                   "https://i.postimg.cc/v8vCXsLQ/Compressed-img-62.jpg",
                   "https://i.postimg.cc/Vv4TNqLS/Compressed-img-63.jpg",
                   "https://i.postimg.cc/nccgPP0q/Compressed-img-64.jpg",
                   "https://i.postimg.cc/SNT3Ffv3/Compressed-img-65.jpg",
                   "https://i.postimg.cc/VkJTYby6/Compressed-img-66.jpg",
                   "https://i.postimg.cc/Ssht7Tn2/Compressed-img-67.jpg",
                   "https://i.postimg.cc/kgLHDX9y/Compressed-img-68.jpg",
                   "https://i.postimg.cc/N0TzXqjv/Compressed-img-69.jpg",
                   "https://i.postimg.cc/HnSZmTBX/Compressed-img-70.jpg",
                   "https://i.postimg.cc/85mXyRvy/Compressed-img-71.jpg",
                   "https://i.postimg.cc/5y97DXqf/Compressed-img-72.jpg",
                   "https://i.postimg.cc/RCGbKT4h/Compressed-img-73.jpg",
                   "https://i.postimg.cc/X7zHD7Z0/Compressed-img-74.jpg",
                   "https://i.postimg.cc/pXTcZnLZ/Compressed-img-75.jpg",
                   "https://i.postimg.cc/hPW5JV4S/Compressed-img-100.jpg",
                   "https://i.postimg.cc/BnJ7ps1k/Compressed-img-101.jpg",
                   "https://i.postimg.cc/L6t0jhhj/Compressed-img-102.jpg",
                   "https://i.postimg.cc/mD1mkg0z/Compressed-img-103.jpg",
                   "https://i.postimg.cc/T3Q7HSVw/Compressed-img-104.jpg",
                   "https://i.postimg.cc/HLxZG2zt/Compressed-img-105.jpg",
                   "https://i.postimg.cc/7hvm2ykB/Compressed-img-106.jpg",
                   "https://i.postimg.cc/90G1PNXc/Compressed-img-107.jpg",
                   "https://i.postimg.cc/MZRs8X7g/Compressed-img-108.jpg",
                   "https://i.postimg.cc/hPB24gMv/Compressed-img-109.jpg",
                   "https://i.postimg.cc/90v1yHH8/Compressed-img-76.jpg",
                   "https://i.postimg.cc/Xqykj1Bw/Compressed-img-78.jpg",
                   "https://i.postimg.cc/s2VmYJbr/Compressed-img-79.jpg",
                   "https://i.postimg.cc/nhKT9WR2/Compressed-img-80.jpg",
                   "https://i.postimg.cc/MKQ9qH1h/Compressed-img-81.jpg",
                   "https://i.postimg.cc/W1cX3Vnt/Compressed-img-82.jpg",
                   "https://i.postimg.cc/xj76wMNv/Compressed-img-83.jpg",
                   "https://i.postimg.cc/C154txFr/Compressed-img-84.jpg",
                   "https://i.postimg.cc/g0NDNZP6/Compressed-img-85.jpg",
                   "https://i.postimg.cc/k4HydPGJ/Compressed-img-86.jpg",
                   "https://i.postimg.cc/rFx7gQZ0/Compressed-img-87.jpg",
                   "https://i.postimg.cc/pybYpQK3/Compressed-img-88.jpg",
                   "https://i.postimg.cc/fRvpQkNM/Compressed-img-89.jpg",
                   "https://i.postimg.cc/dVFpfrgW/Compressed-img-90.jpg",
                   "https://i.postimg.cc/mrXnhqkq/Compressed-img-91.jpg",
                   "https://i.postimg.cc/59HhQxwm/Compressed-img-92.jpg",
                   "https://i.postimg.cc/7Pppgp9r/Compressed-img-93.jpg",
                   "https://i.postimg.cc/MGK46x6V/Compressed-img-94.jpg",
                   "https://i.postimg.cc/1t8jFHNz/Compressed-img-95.jpg",
                   "https://i.postimg.cc/yd2ryZFy/Compressed-img-96.jpg",
                   "https://i.postimg.cc/gjRtS2sF/Compressed-img-97.jpg",
                   "https://i.postimg.cc/v86KH0sq/Compressed-img-98.jpg",
                   "https://i.postimg.cc/43S8X9FR/Compressed-img-99.jpg"]

        img_random = random.randrange(len(img_url))
        print(f'img number ===> {img_random}')
        print('PASSED 1/2')
        while 1:
            a = '.' * i
            try:
                print('Getting Data')
                res_data = session.get(img_url[img_random])
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            except requests.exceptions.Timeout:
                print('Send Screenshot to (NotHere Yeah)')
                print('Error #1')
                sys.exit()
            except ConnectionAbortedError:
                print('Send Screenshot to (NotHere Yeah)')
                print('Error #2')
                sys.exit()
            except requests.execptions.ChunkedEncodingError:
                print('Send Screenshot to (NotHere Yeah)')
                print('Error #3')
                sys.exit()
            except urllib3.exceptions.ProtocolError:
                print('Send Screenshot to (NotHere Yeah)')
                print('Error #4')
                sys.exit()
            time.sleep(1)

        resource_url = 'https://upload.twitter.com/1.1/media/upload.json'
        print('PASSED 2/2')
        upload_image = {
            'media': res_data.content,
            'media_category': 'tweet_image'}

        while 1:
            a = '.' * i
            try:
                media_id = session.post(resource_url, headers=headers, files=upload_image)
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        x = json.loads(media_id.content.decode('UTF-8'))
        save_id = x['media_id']

        while 1:
            a = '.' * i
            try:
                SEND_IMG = session.post('https://twitter.com/i/api/graphql/Mvpg1U7PrmuHeYdY_83kLw/CreateTweet',
                                        headers=headers,
                                        json={"variables": {"tweet_text": Tweet_Text, "media": {
                                            "media_entities": [{"media_id": save_id, "tagged_users": []}],
                                            "possibly_sensitive": 'false'}, "withDownvotePerspective": 'false',
                                                            "withReactionsMetadata": 'false',
                                                            "withReactionsPerspective": 'false',
                                                            "withSuperFollowsTweetFields": 'true',
                                                            "withSuperFollowsUserFields": 'true',
                                                            "semantic_annotation_ids": [],
                                                            "dark_request": 'false'},
                                              "features": {"dont_mention_me_view_api_enabled": 'true',
                                                           "interactive_text_enabled": 'true',
                                                           "responsive_web_uc_gql_enabled": 'false',
                                                           "vibe_api_enabled": 'false',
                                                           "responsive_web_edit_tweet_api_enabled": 'false',
                                                           "standardized_nudges_misinfo": 'true',
                                                           "responsive_web_enhance_cards_enabled": 'false'},
                                              "queryId": "hC1nuE-2d1NX5LYBuuAvtQ"})
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        print(f'{bcolors.OKGREEN}\rTWEET_WITH_IMG_SEND{bcolors.BOLD}\n')

        number_of_tweet += 1

        Timer_Countdown = random.randint(30, 40)

    time.sleep(1)
