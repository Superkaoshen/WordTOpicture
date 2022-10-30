from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# 文字转图片
# 需要的参数： 需要转成图片的文字 字体 保存图片的路径
txt_path = './document.txt'
ttf_path = './ZhupipiHand-Bold.ttf'
save_path = './pic/'


def wordtopicture(txt_path, ttf_path, save_path):
    font = ImageFont.truetype(ttf_path, 24)  # 设置字体和大小
    doc = open(txt_path, 'r', encoding='utf-8')
    string = doc.read()
    doc.close()
    length = len(string)
    print(length)  # 测试数量
    page = 1
    flag = 0  # 字体数量指针
    while flag < length:
        im = Image.open('./12.png')
        draw = ImageDraw.Draw(im)  # 创建draw对象
        for i in range(28):  # 行数
            for j in range(38):  # 列数
                if flag >= length:
                    break
                if string[flag] == '\n':
                    flag = flag + 1
                    break
                draw.text((65 + 20 * j, 80 + i * 48), string[flag], (0, 0, 0),
                          font=font)

                flag = flag + 1
            if flag >= length:
                break
        im.save(save_path + str(page) + ".png")
        im.show()
        page = page + 1


wordtopicture(txt_path, ttf_path, save_path)
print('Success!')
