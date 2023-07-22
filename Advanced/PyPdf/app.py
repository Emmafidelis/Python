import pypdf

merger = pypdf.PdfMerger()
file_names = ["first.pdf", "second.pdf"]
for file_name in file_names:
  merger.append(file_name)
merger.write("combined.pdf")

# with open("first.pdf", "rb") as file:
#   reader = pypdf.PdfReader(file)
#   # print(len(reader.pages))
#   page = reader.pages[0]
#   page.rotate(90)
#   writer = pypdf.PdfWriter()
#   writer.add_page(page)
#   with open("rotated.pdf", "wb") as output:
#     writer.write(output)