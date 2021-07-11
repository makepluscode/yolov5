python3 train.py --img 416 --batch 16 --epochs 5 --data ./dataset/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name gun_yolov5s_results

python3 detect.py --weights ./runs/train/gun_yolov5s_results7/weights/best.pt --img 416 --conf 0.5 --source 0