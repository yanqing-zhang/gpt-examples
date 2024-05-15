import pdfplumber
import pandas as pd
pdf = pdfplumber.open("./The_Old_Man_of_the_Sea.pdf")

md = pdf.metadata

print(f'md:{md}')
"""
md结果如下：
{
    "CreationDate": "D:20060717205532+08'00'",
    "Subject": "For Personal Learning!",
    "Author": "Asiaing.com",
    "Creator": "PScript5.dll Version 5.2",
    "Producer": "Acrobat Distiller 7.0.5 (Windows)",
    "ModDate": "D:20060717210222+08'00'",
    "Title": "Hemingway, Ernest - The Old Man and the Sea"
}
"""

pages = pdf.pages
print(f'pages:{pages}')

page0 = pdf.pages[0]
print(f'page0:{page0}')
# -~==========================================
testpdf = pdfplumber.open("./test.pdf")

ps = testpdf.pages
page_num = ps[0].page_number
print(f'page_num:{page_num}')
width = ps[0].width
height = ps[0].height
print(f'width:{width}, height:{height}')

imag = ps[0].to_image()
# imag.show()

txt0 = ps[0].extract_text()
print(f'txt0:\n{txt0}')
txt0_table = ps[0].extract_text(layout=True)
print(f'txt0_table:\n{txt0_table}')

# 提取table
txt_table2 = ps[0].extract_table()
print(f'txt_table2:\n{txt_table2}')

# table 转 dataframe
df = pd.DataFrame(txt_table2[1:], columns=txt_table2[0])
print(f'df:\n{df}')

img = ps[1].images[0]
bbox = (img["x0"], img["top"], img["x1"], img["bottom"])
cropped_page = ps[1].crop(bbox)
cropped_page.to_image()
cropped_page.to_image(antialias=True)
cropped_page.to_image(resolution=1080)
im = cropped_page.to_image(antialias=True)
im.save("pdf_image_test.png")
im.show()