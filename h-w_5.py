# п.5 Є рядок, в якому зберігаються 1000 слів. Створіть словник із ключами - унікальними словами та значеннями
# - кількістю повторів кожного слова у послідовності.
str1 = ("Lorem ipsum dolor sit amet consectetur adipiscing elit Aliquam lacus metus sodales vitae eros ac "
        "convallis accumsan erat Aenean sem sapien faucibus at est ut varius bibendum mi Quisque a iaculis augue"
        " Vestibulum quis turpis bibendum libero condimentum commodo Curabitur pulvinar nisl elit ut feugiat mauris "
        "pharetra vitae Sed accumsan at risus nec finibus Fusce vestibulum suscipit diam non commodo "
        "Nullam eget efficitur velit Mauris vel dui est Suspendisse potenti Mauris vitae tempor velit "
        "Etiam vel augue vitae orci dictum vestibulum Proin sagittis pharetra ultricies "
        "Donec pretium orci ac tempus tincidunt Nam nec lacinia justo Nullam molestie nulla orci "
        "id facilisis risus auctor eu Class aptent taciti sociosqu ad litora torquent per conubia nostra "
        "per inceptos himenaeos Maecenas ut tempus ipsum Phasellus vitae nibh nulla Mauris nec facilisis metus "
        "Morbi aliquet nec mi quis ultricies Pellentesque euismod placerat urna eget interdum Aenean mi magna "
        "sagittis ac viverra vel tristique non nunc Donec elementum mauris quis tristique blandit "
        "Suspendisse laoreet mattis mi ac congue Suspendisse vitae magna a nulla faucibus ultrices "
        "Vivamus dapibus finibus laoreet Praesent et sapien arcu Cras nec tortor dignissim accumsan lorem et "
        "imperdiet purus Ut sit amet dui finibus maximus sem ac aliquam elit Nam malesuada sem nec iaculis "
        "rhoncus ante sapien tincidunt ante ac hendrerit sem mi vel ligula Duis varius ligula sit amet magna porta "
        "eu pretium justo sollicitudin Nullam vulputate eu nibh sit amet viverra Ut id mi a nisi vestibulum iaculis "
        "Curabitur convallis libero tellus eu molestie quam bibendum non Nullam ac euismod dui vel bibendum augue "
        "Duis condimentum bibendum laoreet Suspendisse pulvinar tempor elit vel scelerisque In hac habitasse "
        "platea dictumst Nam porttitor leo a tincidunt porttitor Sed commodo augue ut mi sagittis scelerisque "
        "Quisque molestie commodo auctor Fusce maximus commodo venenatis Nullam aliquet magna vitae iaculis "
        "tincidunt Aenean suscipit ut felis at hendrerit Interdum et malesuada fames ac ante ipsum primis in "
        "faucibus Suspendisse aliquet nisl vel consequat accumsan ex nibh iaculis sem pharetra blandit nulla "
        "tellus eu mauris Maecenas vitae velit in nunc porttitor pellentesque Proin et felis hendrerit bibendum "
        "urna at auctor nuncPhasellus ut libero sit amet felis sodales faucibus quis nec lectus Donec sed suscipit "
        "dui Donec dictum magna at bibendum gravida Nunc dignissim placerat euismod Maecenas vestibulum lacinia "
        "mauris Nulla quis turpis metus Pellentesque sagittis diam quis sodales consectetur Vivamus felis velit "
        "posuere facilisis velit non tempus pharetra lorem Sed eget mauris et ipsum posuere bibendum Sed blandit "
        "sit amet ante a sollicitudin Suspendisse suscipit lorem sed luctus lobortis Nulla id hendrerit nisl "
        "Morbi in imperdiet justo non accumsan justo Sed sit amet rhoncus ligula Pellentesque facilisis ut urna "
        "vel convallis Proin urna lacus cursus nec dictum quis aliquam sed lacus Nulla eleifend velit ac semper"
        " ullamcorper sapien ipsum laoreet augue id interdum augue metus vitae metus Etiam consequat dignissim "
        "neque vitae fermentum nisl placerat et Aliquam rutrum metus et aliquam tempor mi augue egestas dolor "
        "id auctor felis lectus eu tortor Nunc quis fringilla urna Cras ornare laoreet molestie Nunc ullamcorper "
        "ipsum mauris quis venenatis augue ultrices rutrum Duis vitae dignissim erat Aenean ac vulputate turpis "
        "Praesent sem ante congue sit amet leo sed bibendum rutrum diam Maecenas iaculis metus non mauris "
        "luctus vestibulum Maecenas suscipit varius tellus vitae tincidunt neque tempor nec Quisque tincidunt "
        "lobortis erat in feugiat risus pretium nec Phasellus at bibendum arcu volutpat porttitor enim "
        "Morbi bibendum porta justo vel placerat Vestibulum ante ipsum primis in faucibus orci luctus et ultrices "
        "posuere cubilia curae; Sed et nibh feugiat vehicula massa a facilisis nibh Proin risus arcu mollis "
        "semper ipsum non luctus convallis urna Fusce vel orci semper lectus tempor aliquam in tincidunt augue "
        "Aliquam at pulvinar massa quis posuere ante Proin odio ipsum ultricies id massa eu accumsan "
        "imperdiet ex Mauris lorem dui lacinia in lobortis vel tincidunt nec risus Cras condimentum erat "
        "vitae ligula vehicula condimentum Quisque placerat eros accumsan posuere dolor at fermentum lectus "
        "Etiam tempus mauris a lectus venenatis quis rutrum odio vestibulum Vivamus sed metus metus "
        "Duis euismod ornare condimentum Nullam id viverra ante Aliquam erat volutpat Aenean vel ligula tincidunt "
        "porttitor turpis et commodo dui Quisque tempus eros quis dolor gravida scelerisque Pellentesque interdum "
        "tellus in porta accumsan Aenean tincidunt est id rhoncus facilisis dolor odio molestie neque  posuere "
        "dui est non orci Mauris suscipit magna eu eros placerat mattis Vestibulum auctor purus aliquam ante "
        "ultrices congue Curabitur pellentesque erat sed consectetur varius turpis tellus gravida sem nec "
        "scelerisque mi enim eu felis Nulla accumsan massa non iaculis dapibus lectus mi aliquam lectus sit "
        "amet ornare libero metus ut lectus Sed iaculis blandit varius Sed efficitur quis lorem vitae dapibus "
        "Vestibulum nec pretium nisl vel iaculis ante Etiam maximus sapien justo eget tempor mi lobortis mattis "
        "Fusce sit amet urna in leo venenatis tristique vitae in lorem Donec eget tincidunt eros ac finibus erat"
        "Mauris a lacus eu nisl posuere condimentum sit amet id turpis Mauris augue tortor volutpat in rutrum et "
        "dignissim vel elit In sollicitudin diam dolor ac elementum erat consectetur quis Phasellus varius semper "
        "metus id rhoncus Duis lacinia posuere purus cursus luctus Praesent vulputate molestie nisl nec maximus "
        "eros maximus viverra Sed diam ex ornare at erat sit amet placerat cursus orci Integer egestas erat erat "
        "ac tristique erat suscipit sit amet Sed id convallis leo a tincidunt lectus In fringilla leo in suscipit "
        "tincidunt est mauris volutpat dui sed placerat nulla lacus et turpis Mauris maximus posuere elit ac "
        "laoreet massa vehicula eget Vestibulum placerat ex at congue feugiat ante tortor aliquet diam a luctus "
        "justo purus vitae nunc Nunc ultricies tellus vitae lacus rhoncus tempus accumsan mi laoreet Nunc porttitor "
        "mattis ex et tincidunt Cras non tincidunt lectus Vestibulum lacinia ac risus vitae ornare Morbi sagittis "
        "metus sed sollicitudin porta Duis in felis ultrices dapibus quam vel tincidunt eros Mauris a magna  "
        "luctus mauris sed bibendum nibh Nulla iaculis velit dui ut tincidunt orci pulvinar eget Sed arcu quam "
        "dignissim vel nibh eget rutrum elementum augue Mauris sapien risus pretium ut metus at eleifend iaculis "
        "justo Nam semper Vitae gravida").lower()

list1 = str1.split(" ")
set1 = set(list1)
dict1 = {}
for i in set1:
    count_i = list1.count(i)
    dict1[i] = count_i
print(dict1)