import os, sys
import glob

code_root = sys.argv[1]
pdf_root = sys.argv[2]
h_root = os.path.join(code_root, 'include')
hpp_root = os.path.join(code_root, 'include')
cpp_root = os.path.join(code_root, 'src')

pdf_h_root = os.path.join(pdf_root, 'h')
pdf_hpp_root = os.path.join(pdf_root, 'hpp')
pdf_cpp_root = os.path.join(pdf_root, 'src')

if not os.path.exists(pdf_h_root):
    os.mkdir(pdf_h_root)
if not os.path.exists(pdf_hpp_root):
    os.mkdir(pdf_hpp_root)
if not os.path.exists(pdf_cpp_root):
    os.mkdir(pdf_cpp_root)

h_files = glob.glob(h_root + '/**/*.h', recursive=True)
hpp_files = glob.glob(hpp_root + '/**/*.hpp', recursive=True)
src_files = glob.glob(cpp_root + '/**/*.cpp', recursive=True)

# code2pdf_cmd = 'find . -name "*.h" | xargs enscript -B --color=1 -C -Ecpp -fCourier8 -o - | ps2pdf - code.pdf'

for h in h_files:
    out_pdf = os.path.join(pdf_h_root, os.path.basename(h)+'.pdf')
    cmd = 'enscript -B --color=1 -C -Ecpp -fCourier8 -o - ' + h + ' | ps2pdf - ' + out_pdf
    os.system(cmd)

for h in hpp_files:
    out_pdf = os.path.join(pdf_hpp_root, os.path.basename(h)+'.pdf')
    cmd = 'enscript -B --color=1 -C -Ecpp -fCourier8 -o - ' + h + ' | ps2pdf - ' + out_pdf
    os.system(cmd)

for h in src_files:
    out_pdf = os.path.join(pdf_cpp_root, os.path.basename(h)+'.pdf')
    cmd = 'enscript -B --color=1 -C -Ecpp -fCourier8 -o - ' + h + ' | ps2pdf - ' + out_pdf
    os.system(cmd)