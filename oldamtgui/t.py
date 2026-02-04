import torch

from models import OnsetsAndVelocities 

# print(torch.__version__)

model_path = "models/OnsetsAndVelocities_2023_03_04_09_53_53.289step=43500_f1=0.9675__0.9480.pt"
num_mels=229
num_keys=88,
conv1x1_head=(200, 200)
lrelu_slope=0.1
device="cpu"

model = OnsetsAndVelocities(in_chans=2,
                            in_height=num_mels,
                            out_height=num_keys,
                            conv1x1head=conv1x1_head,
                            bn_momentum=0,
                            leaky_relu_slope=lrelu_slope,
                            dropout_drop_p=0).to(device)

state_dict = torch.load(model_path, map_location=torch.device(device))
model.load_state_dict(state_dict, strict=True)
model.eval()

print(model)



