import pathlib
from fastai2.vision.all import *

def load_posix_learner(model_path):
	save = pathlib.PosixPath.copy()
	pathlib.PosixPath = pathlib.WindowsPath

	learn = load_learner(model_path)

	pathlib.PosixPath = save
	return learn

def save_learner(learner, datablock, source, save_path, **kwargs):
	dls = datablock.dataloaders(source, num_worker=0, **kwargs)
	learner.dls = dls
	learner.export(save_path)
