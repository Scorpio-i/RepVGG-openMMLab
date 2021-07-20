echo "In data/ "
echo "create imagenet/train ..."
mkdir -p imagenet/train
echo "create imagenet/val ..."
mkdir -p imagenet/val
echo "create imagenet/meta ..."
mkdir -p imagenet/meta

cd imagenet/train
echo "=====> ImageNet(train) Downloading..."

wget -c https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar


echo "=====> Unzipping(train)..."

tar -xvf ILSVRC2012_img_train.tar && rm -f ILSVRC2012_img_train.tar

for tar_filename in *.tar;
do
    mkdir -p ${tar_filename:0:9};
    tar -xvf ${tar_filename} -C ${tar_filename:0:9};
    rm -f ${tar_filename};
done;

echo "=====> done. "

cd ../val

echo "=====> ImageNet(val) Downloading..."


wget -c https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_val.tar

echo "=====> Unzipping(val)..."


tar -xvf ILSVRC2012_img_val.tar && rm -f ILSVRC2012_img_val.tar


cd ../meta


echo "=====> ImageNet(meta) Downloading..."

wget -c http://dl.caffe.berkeleyvision.org/caffe_ilsvrc12.tar.gz

echo "=====> Unzipping(meta)..."

tar -xf caffe_ilsvrc12.tar.gz && rm -f caffe_ilsvrc12.tar.gz

echo "Done."