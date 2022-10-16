import pickle
import pandas as pd
from PIL import Image
import streamlit as st
from Comicle_Class import Comic, MainComic, SubComic, FeaturedCharacter


with open('ComicInstances.bin', 'rb') as p:
    ComicInstances = pickle.load(p)

st.title("Comicle")
st.write("***")

if st.sidebar.button("Comicleとは？"):
    st.write("Comicleとは〜。")

st.sidebar.write("***")
st.sidebar.header("漫画作品一覧")
for xComicInstance in ComicInstances:
    xTitle = xComicInstance.get_Title()
    if st.sidebar.button(str(xTitle)):
        st.header("「" + xTitle + "」")
        df1 = pd.DataFrame({
            "作品名":[xTitle],
            "作者名":[xComicInstance.get_Author()],
            "年代":[xComicInstance.get_Era()],
            "出版社":[xComicInstance.get_Publisher()],
            "対象":[xComicInstance.get_Target()],
            "ジャンル":[xComicInstance.get_Genre()],
            "続巻の有無":[xComicInstance.get_Type()]
        })
        st.write(df1.set_index("作品名"))
        st.write("***")

        st.header("「" + xTitle + "」とストーリーラインが類似している漫画10作品")
        SBDComicRanking = xComicInstance.get_SBDComicRanking()[:10]
        Titles, Distances, Authors, Eras, Publishers, Targets, Genres, Types = [], [], [], [], [], [], [], []
        for yComicInstance in SBDComicRanking:
            Titles.append(yComicInstance.get_Title())
            Distances.append(yComicInstance.get_Distance())
            Authors.append(yComicInstance.get_Author())
            Eras.append(yComicInstance.get_Era())
            Publishers.append(yComicInstance.get_Publisher())
            Targets.append(yComicInstance.get_Target())
            Genres.append(yComicInstance.get_Genre())
            Types.append(yComicInstance.get_Type())

        df2 = pd.DataFrame({
            "作品名":Titles,
            "類似度":Distances,
            "作者名":Authors,
            "年代":Eras,
            "出版社":Publishers,
            "対象":Targets,
            "ジャンル":Genres,
            "続巻の有無":Types
        })
        st.write(df2.set_index("作品名"))
        st.write("***")

        st.header("作品毎のストーリーラインの表示")
        for yComicInstance in SBDComicRanking:
            left_column, right_column = st.columns(2)
            yTitle = yComicInstance.get_Title()
            yDistance = yComicInstance.get_Distance()
            xImg = Image.open("Graph/" + xTitle + ".png")
            yImg = Image.open("Graph/" + yTitle + ".png")
            left_column.image(xImg, caption = xTitle, use_column_width = True)
            right_column.image(yImg, caption = yTitle + "(類似度：" + str(yDistance) + ")", use_column_width = True)
            st.write("***")




