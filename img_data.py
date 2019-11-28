#coding=utf-8
from PIL import Image, ImageDraw, ImageFont
# from pythontest import test_dm_cursor_fetchone_003
def draw_image(new_img, text, show_image=False):
    font = ImageFont.truetype(r'C:\Users\Administrator\PycharmProjects\img_set\MSYHMONO.ttf', 15, encoding='utf-8')
    text = str(text)
    draw = ImageDraw.Draw(new_img)
    img_size = new_img.size
    draw.line((0, 0) + img_size, fill=128)
    draw.line((0, img_size[1], img_size[0], 0), fill=128)

    font_size = 40
    fnt = ImageFont.truetype(r'C:\Users\Administrator\PycharmProjects\img_set\MSYHMONO.ttf', font_size, encoding='utf-8')
    fnt_size = fnt.getsize(text)
    while fnt_size[0] > img_size[0] or fnt_size[0] > img_size[0]:
        font_size -= 5
        fnt = ImageFont.truetype(r'C:\Users\Administrator\PycharmProjects\img_set\MSYHMONO.ttf', font_size, encoding='utf-8')
        fnt_size = fnt.getsize(text)

    x = (img_size[0] - fnt_size[0]) / 2
    y = (img_size[1] - fnt_size[1]) / 2
    draw.text((x, y), text, font=fnt, fill=(255, 0, 0))

    if show_image:
        new_img.show()
    del draw


def new_image(width, height, text='default', color=(100, 100, 100, 255), show_image=False):
    font = ImageFont.truetype(r'C:\Users\Administrator\PycharmProjects\img_set\MSYHMONO.ttf', 15, encoding='utf-8')
    new_img = Image.new('RGB', (int(width), int(height)), color)
    draw_image(new_img, text, show_image)
    new_img.save(r'%s.jpg' % (text))
    del new_img


def new_image_with_file(fn):
    with open(fn, encoding='utf-8') as f:
        for l in f:
            l = l.strip()
            if l:
                ls = l.split(',')
                if '#' == l[0] or len(ls) < 2:
                    continue
                new_image(*ls)

def tset_img(id, name, str_time):
    # import unicode
    from prettytable import PrettyTable
    from PIL import Image, ImageDraw, ImageFont
    tab = PrettyTable()
    # 设置表头
    tab.field_names = ["id", "name", "time"]
    # 表格内容插入
    tab.add_row([id, name, str_time])

    tab_info = str(tab)
    space = 5

    # PIL模块中，确定写入到图片中的文本字体
    font = ImageFont.truetype(r'C:\Users\Administrator\PycharmProjects\img_set\MSYHMONO.ttf', 15, encoding='utf-8')
    # Image模块创建一个图片对象
    im = Image.new('RGB', (10, 10), (0, 0, 0, 0))
    # ImageDraw向图片中进行操作，写入文字或者插入线条都可以
    draw = ImageDraw.Draw(im, "RGB")
    # 根据插入图片中的文字内容和字体信息，来确定图片的最终大小
    img_size = draw.multiline_textsize(tab_info, font=font)
    # 图片初始化的大小为10-10，现在根据图片内容要重新设置图片的大小
    im_new = im.resize((img_size[0] + space * 2, img_size[1] + space * 2))
    del draw
    del im
    draw = ImageDraw.Draw(im_new, 'RGB')
    # 批量写入到图片中，这里的multiline_text会自动识别换行符
    # python2
    draw.multiline_text((space, space),  tab_info , fill=(255, 255, 255), font=font)
    # python3
    # draw.multiline_text((space,space), tab_info, fill=(255,255,255), font=font)
    file_name = str(id) + "_" + str(name) + "_" + str(str_time)+".jpg"

    im_new.save( file_name)
    del draw




if '__main__' == __name__:
    # usertlist =  test_dm_cursor_fetchone_003()
    # id_list=[]
    # id_dir={}
    # for user in usertlist:
    #     id_list.append(user.id)
    #     id_dir["id_dir"] = str(user.CZRKGMSFHM) +"_"+str(user.CZRKXM)+"_"+str(user.CZRKXPRKSJ)
    # # 去重
    # new_id_list = set(id_list)
    # for new_id in new_id_list:
    #     txt = id_dir[new_id]
    #     # 身份证号字段_姓名_入库时间.jpg
    # new_image(400, 300, '身份证号字段_姓名_入库时间', show_image=False)
    # new_image_with_file('image_data.txt')
    tset_img("身份证号字段","姓名","入库时间2")


