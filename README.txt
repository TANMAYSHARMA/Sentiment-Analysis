Title: Sentiment Analysis With Recurrent Neural Networks

Project submitted by:
Ankit Sinha (UIN: 671342169)
Tanmay Sharma (UIN: 659840235)
Vaidehi Deshmukh (UIN: 656205552)

This project consists of the following files:
1. train.py
2. preprocessing.py
3. Models: vRNN.py, GRU.py, LSTM.py, attn_RNN.py
4. Shell scripts: run_vRNN.sh, run_GRU.sh, run_LSTM.sh, run_attnRNN.sh
5. IDS576_Project.ipynb
6. hotel_reviews_preprocessed.csv
	
Instructions for running a model:
1. Set desired parameters in the model's shell script
2. Open IDS576_Project.ipynb
3. Run blocks for environment setup
4. Run the code block containing bash command for the model's shell script
5. A log file and saved model with .pt extension are created automatically for the current execution

Description of model parameters can be found in train.py file. The submitted shell scripts have the parameters that gave best performance in our testing. Please take notice of the note included in the aforementioned file that states that before executing additive attention model you need to run one of the other non-attention models to avoid an unexplained runtime error. We tried to resolve this runtime error of binary cross entropy loss but we couldn't figure out why it would throw that error every time only on the first run. We have included just the preprocessed file because the raw file is over 200 MB in size. Although, the original data can be downloaded from the link provided in preprocessing.py, which includes the first part of preprocessing. The other half of preprocessing is done in train.py using torchtext.
