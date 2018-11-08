import codecs


def rf(file):
    with codecs.open(fn,encoding='utf-8') as f:
        return f.readlines()

def transform(fn,choices,title):
    print('form.addPageBreakItem().setTitle(\'{0}\');'.format(title))
    print('var choices = [{0}];'.format(",".join(["\""+x+"\"" for x in choices])))
    for x in rf(fn):
        x = x.strip()
        print('item = \"{0}\";'.format(x))
        print('form.addMultipleChoiceItem().setTitle(item).setChoiceValues(choices).setRequired(true);')

def transform2(fn,title):
    print('var title = (\'{0}\');'.format(title))
    print('form.addPageBreakItem().setTitle(\'{0}\');'.format(title))
    n=0
    for x in rf(fn):
        if n%2==0:
            a=x
        else:
            x = x.strip()
            print('item = \"{0}\";'.format(x))
            print('form.addMultipleChoiceItem().setTitle(title).setChoiceValues(a,x).setRequired(true);')
        n+=1

transform2('part2.txt', "Отметьте нужный ответ")



transform('part5.txt',["Не согласен", "Скорее не согласен", "Не знаю", "Скорее согласен", "Cогласен"],"Отметьте нужный ответ")
transform('part6.txt',["Категорически не согласен","Не согласен", "Скорее не согласен", "Не знаю", "Скорее согласен", "Cогласен","Полностью согласен"],"Оцените степень согласия со следующими утверждениями по шкале от «категорически не согласен» до «полностью согласен».")
transform('part7.txt',["Совсем не похожа на меня", "Не похожа на меня", "Совсем чуть-чуть похожа на меня", "Немного похожа на меня", "В значительной степени похожа на меня", "Очень похожа на меня"],"На этот опросник отвечают только девушки")
transform('part1.txt',["Совсем не похож на меня", "Не похож на меня", "Совсем чуть-чуть похож на меня", "Немного похож на меня", "В значительной степени похож на меня", "Очень похож на меня"],"На этот опросник отвечают только юноши")
transform('part3.txt',["Не согласен", "Скорее не согласен", "Не знаю", "Скорее согласен", "Cогласен"],"Ответьте, пожалуйста, на следующие утверждения так, как ответили бы на них люди, которые старше Вас на 10 лет и добились успеха.")
transform('part4.txt',["Да","Нет"],"Отметьте нужный ответ")
transform2('part2.txt',["Да","Нет"],"Отметьте нужный ответ")

