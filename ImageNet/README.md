# ImageNet Dataset Preprocess

These preprocess steps mainly target Pytorch

### Step1

Download training dataset and validation dataset

* Download ILSVRC201 Dataset from [Imagenet](http://www.image-net.org/challenges/LSVRC/2012/nonpub-downloads)

  * Download Training Dataset on Task 1&2
  * Download Validation Dataset on Task 1&2
  * No need to download Test Dataset or Development Kit or Bounding Boxes
  
After this, you will have `ILSVRC2012_img.train.tar` and `ILSVRC2012_img.val.tar`

### Step2

Extract training dataset

* Create a folder `/path/to/imagenet/train/folder`

* Extract the train tar to the folder, this will generate lots of .tar files in `xxx/folder`
  ```sh
  tar -xf ILSVRC2012_img.train.tar -C /path/to/imagenet/train/folder
  ```

* Run following commands to extract .tar in folder
  ```
  cd /path/to/imagenet/train/folder
  wget 
  chmod u+x extract.sh
  ./extract.sh
  ```
  This will extract all the .tar files in `xx/folder` and put them (folders' names start from 'n0xxxx') under `/path/to/imagenet/train/` and remove `/path/to/imagenet/train/folder`

Now training folder is done.

### Step3

Extract validation dataset

* Create a folder `/path/to/imagenet/val/`

* Extract the test tar to the val foler with the following commands:
  ```sh
  tar -xf ILSVRC2012_img.val.tar -C /path/to/imagenet/val/
  ```
  This will generate lots of .JPEG files

* Format them just like train folder:
  ```sh
  cd /path/to/imagenet/val/
  wget https://raw.githubusercontent.com/soumith/imagenetloader.torch/master/valprep.sh
  chmod u+x valprep.sh
  ./valprep.sh
  rm valprep.sh
  ```
  Then you won't see any `.JPEG` files in `/path/to/imagenet/val/`, instead, you will see a lot of folders named starting from 'n0xxxx' just like `/path/to/imagenet/train/`

Now validation folder is done.

All preprcess for downloaded raw ImageNet dataset are now finished.
