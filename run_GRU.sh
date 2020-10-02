python -u train.py \
    --model GRU \
    --epochs 5 \
    --lr 0.01 \
    --weight-decay 0.0 \
    --batch-size 500 \
    --hidden_dim 100 \
    --dropout 0.0 \
    --num_layers 1 \
    --useGlove False \
    --trainable False \
    --bidirectional False \
    --typeOfPadding pack_padded | tee GRU.log