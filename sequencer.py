from reader import read_file
from writer import write_file
from processer import split_with_eos


inpath = "src/sample/sample.txt"
outpath = "src/sample/sample_out.txt"

f_str = split_with_eos(f_str=read_file(path=inpath))
write_file(path=outpath, contents=f_str)