CUDA_VISIBLE_DEVICES=1,2,3,4 python train.py --img 1280 --batch 12 --epochs 200 --data coco128.yaml --cfg /home/noman/yolov5x/models/yolov5x.yaml  --weights runs/train/exp2/weights/best.pt





CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7,8 python train.py --img 1280 --batch 16 --epochs 200 --data coco128.yaml --cfg models/yolov5x_new.yaml  --weights yolov5x.pt


CUDA_VISIBLE_DEVICES=0,1,2,3 python detect.py --img 1280 --weights /home/noman/yolov5-master/yolov5-master/runs/train/exp8/weights/last.pt --half --source /home/noman/public_testset_images/test2_images --save-txt --save-conf

CUDA_VISIBLE_DEVICES=0,1,2,3 python detect.py --img 1280 --weights runs/train/exp23/weights/last.pt runs/train/exp24/weights/last.pt --half --source /home/noman/public_testset_images/test2_images --save-txt --save-conf



/home/noman/datanew/private_test_set_1/test_set_1/images
