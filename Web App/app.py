import streamlit as st
import joblib

@st.cache(allow_output_mutation=True)
def get_model():
    from tensorflow.keras.models import load_model
    model=load_model('model.h5')
    return model


def main():

    html_temp = """
    <div style="background-color:cyan;padding:10px">
    <h2 style="color:black;text-align:center;">Petrol Price Predictor</h2>
    </div>
           """

    st.markdown(html_temp,unsafe_allow_html=True)

    year = st.text_input("Year","Type Here")

    month = st.text_input('Month','type here')

    if st.button("Predict"):
        model = joblib.load("rf_model.joblib")
        result = model.predict([[month, year]])[0]

        st.success(result)


if __name__=='__main__':
    main()

