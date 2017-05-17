pypy sample_va.py
../../../myml/libsffm-apk-softmax/ffm-train-predict  --auto-stop -savefield 13 --hasLabel  -fmap feamap.txt --trainbatch -t 1 -l 0.00009 -r 0.05  -decay 0.02 -s 8 -k 4 -p cvdata/va_sample.fm -test cvdata/va.fm -out cv.csv  cvdata/tr.fm cv-model
