import streamlit as st
import os
from PIL import Image
import shutil
from prediction_utils import predict_image_class
import base64
from pathlib import Path

if os.path.exists(os.path.join(os.getcwd(), "uploaded_img_dir")):
    shutil.rmtree(os.path.join(os.getcwd(), "uploaded_img_dir"))

os.mkdir(os.path.join(os.getcwd(), "uploaded_img_dir"))


def save_image(image_file):
    @st.cache_data
    def load_image(image_file):
        img = Image.open(image_file)
        return img

    img = load_image(image_file)

    with open(os.path.join(os.getcwd(), "uploaded_img_dir",image_file.name), "wb") as f:
        f.write(image_file.getbuffer())

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html

add_selectbox = st.sidebar.selectbox(
    "Select ",
    ("Demo Info", "Demo")
)
st.markdown("<p style='text-align: right; color: white;'> "+img_to_html('kpmg.png')+"</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'> "+img_to_html('national_emblem_resized.png')+"</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: blue;'>Computer Vision Demo</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>KPMG DEMO</h3>", unsafe_allow_html=True)
st.write("\n\n\n\n\n")
st.write("\n\n\n\n\n")
st.write("\n\n\n\n\n")

st.markdown("<h2 style='text-align: center; color: blue;'>Skin Disease Classification</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Acne and Actinic Skin Disease Classification </h4>", unsafe_allow_html=True)

if add_selectbox == "Demo Info":

    # display the text if the checkbox returns True value
    html_acne = """
        <div style="background-color:#00008B ;font-size:24px;padding:24px">
        <h3 style="color:white;text-align:center;"><b>Acne Skin Condition</b></h3>
        <h4 style="color:white;text-align:center;">Acne is a skin condition that occurs when your hair follicles become plugged with oil and dead skin cells. It causes whiteheads, blackheads or pimples. Acne is most common among teenagers, though it affects people of all ages. Effective acne treatments are available, but acne can be persistent. The pimples and bumps heal slowly, and when one begins to go away, others seem to crop up. Depending on its severity, acne can cause emotional distress and scar the skin. The earlier you start treatment, the lower your risk of such problems</h4>
        </div>
            """
    st.markdown(html_acne, unsafe_allow_html=True)

    html_actinic = """
            <div style="background-color:#00008B ;font-size:24px;padding:24px">
            <h3 style="color:white;text-align:center;"><b>Actinic Skin Condition</b></h3>
            <h4 style="color:white;text-align:center;">Actinic keratosis is a rough, scaly patch or bump on the skin. It’s also known as a solar keratosis. Actinic keratoses are very common, and many people have them. They are caused by ultraviolet (UV) damage to the skin. Some actinic keratoses can turn into squamous cell skin cancer. Because of this, the lesions are often called precancer. They are not life-threatening. But if they are found and treated early, they do not have the chance to develop into skin cancer.</h4>
            </div>
                """
    st.markdown(html_actinic, unsafe_allow_html=True)

    html_melanoma = """
                <div style="background-color:#00008B ;font-size:24px;padding:24px">
                <h3 style="color:white;text-align:center;"><b>Actinic Skin Condition</b></h3>
                <h4 style="color:white;text-align:center;">Melanoma is a kind of skin cancer that starts in the melanocytes. Melanocytes are cells that make the pigment that gives skin its color. The pigment is called melanin. Melanoma typically starts on skin that's often exposed to the sun. This includes the skin on the arms, back, face and legs. Melanoma also can form in the eyes. Rarely, it can happen inside the body, such as in the nose or throat. The exact cause of all melanomas isn't clear. Most melanomas are caused by exposure to ultraviolet light. Ultraviolet light, also called UV light, comes from sunlight or tanning lamps and beds. Limiting exposure to UV light can help reduce the risk of melanoma. The risk of melanoma seems to be increasing in people under 40, especially women. Knowing the symptoms of skin cancer can help ensure that cancerous changes are detected and treated before the cancer has spread. Melanoma can be treated successfully if it is found early.</h4>
                </div>
                    """
    #st.markdown(html_melanoma, unsafe_allow_html=True)

else:
    skin_disease_image = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])
    if skin_disease_image is not None:
        file_details = {"FileName": skin_disease_image.name, "FileType": skin_disease_image.type}
        st.write(file_details)
        save_image(skin_disease_image)
        st.success(" Image File Saved")
        submit = st.button('Get Prediction')
        if submit:
            with st.spinner(text="This may take a moment..."):
                uploaded_image = os.listdir(os.path.join(os.getcwd(), "uploaded_img_dir"))
                uploaded_image_file_path = os.path.join(os.getcwd(), "uploaded_img_dir", uploaded_image[0])
                st.image(Image.open(uploaded_image_file_path))
                prediction = predict_image_class(uploaded_image_file_path)

            st.write("This image most likely belongs to", prediction)

    else:
        st.write("Please Upload Image")



