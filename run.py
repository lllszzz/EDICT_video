from edict_functions import *

def plot_EDICT_outputs(img1,img2,img3,num):
    width1, height1 = img1.size
    width2, height2 = img2.size
    width3, height3 = img3.size

    new_width = width1 + width2
    new_height = height1 + height3

    new_image = Image.new('RGB', (new_width, new_height),(0,0,0))

    new_image.paste(img1, (0, 0))
    new_image.paste(img2, (width1, 0))
    new_image.paste(img3, (0, height1))

    new_image.save(f'result_2/j_{str(num)}.png')

def run_i2i():
    base_prompt = 'a black swan with a red beak swimming in a river near a wall and bushes'
    edit_prompt = 'a white duck with a yellow beak swimming in a river near a wall and bushes'

    for i in range(8):
        print(f'Start frame {str(i)}')
        im_path = f'experiment_images/shape/swan_swarov/0000{str(i)}.png'
        ori_img = load_im_into_format_from_path(im_path)
        edit_img = EDICT_editing(im_path = im_path, base_prompt = base_prompt, edit_prompt = edit_prompt, steps = 50)[0]
        rec_img = EDICT_editing(im_path = im_path, base_prompt = base_prompt, edit_prompt = base_prompt, steps = 50)[0]
        plot_EDICT_outputs(ori_img,rec_img,edit_img,i)
        print(f'Finish frame {str(i)}')

def run_v2v():
    base_prompt = 'a black swan with a red beak swimming in a river near a wall and bushes'
    edit_prompt = 'a white duck with a yellow beak swimming in a river near a wall and bushes'

    im_path = f'experiment_images/shape/swan_swarov'
    ori_img = load_im_into_format_from_path(im_path)
    edit_img = EDICT_editing(im_path = im_path, base_prompt = base_prompt, edit_prompt = edit_prompt, steps = 50)[0]
    rec_img = EDICT_editing(im_path = im_path, base_prompt = base_prompt, edit_prompt = base_prompt, steps = 50)[0]
    for i in range(4):
        plot_EDICT_outputs(ori_img[2*i],rec_img[i],edit_img[i],i)


if __name__ == "__main__":
    # run_i2i()
    run_v2v()
