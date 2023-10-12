## Improving Private Representations of Text by Mitigating Information Leakage

This README file provides instructions on how to run our model and corresponding baselines. There are a couple files to note here. The dataset folder contains our raw unprocessed data which is then processed using blog_data_reader.py. Our model resides in `DisentangledVAE.ipynb` and our baseline models are in `Baselines.ipynb`


### Our Model

Our model can essentially be run with untuned hyper-parameter if  you run the `DisentangledVAE.ipynb` notebook from top to bottom in Co-lab. If you wish to tune the hyper-parameters, please note the `train_params` dictionary in the last cell
```
{
	'epochs': 100,
	'adv_lr': 1e-4,
	'adv_weight_decay': 1e-3,
	'dis_lr': 1e-3,
	'dis_weight_decay': 1e-4,
	'kl_weight': 1e-3,
	'target_server_weight': 1,
	'target_adversary_weight': 1,
	'sensitive_server_weight': 1,
	'sensitive_adversary_weight': 1
}
```
Terms prefixed by `adv` and `dis` refer to the learning rate and weight decay parameters for the adversary and disentangler optimization step respectively: more details about the two step approach in the paper. Terms suffixed by `weight` are basically a multiplication constant used to weigh each term in the loss function to tune the privacy-utility tradeoff.

### Baselines
Our `Baselines.ipynb` file also contains a few baselines in which we compare our model to including the SOTA Model (Coavaux et. al, 2018), our model without the Variational Encoder, and simple classification models for target and sensitive attributes without obfuscation. All the baselines with untuned hyperparameters can be run if the `Baselines.ipynb` file is run from top to bottom in Co-lab. 

### Packages
These notebooks should run directly in Co-Lab. No packages outside of the ones in Co-Lab or the ones we install through the notebooks are necessary.
### Note: Please save in a folder called `287 Project` before uploading to Co-Lab to prevent having to modify the mount, please also uncompress the `blog_dataset.zip` file which you can find in the Canvas submission (too large for Github)
