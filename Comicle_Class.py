class Comic:
    def __init__(self, File, Title, Author, Era, Publisher, Target, Genre, Type):
        self.File = File
        self.Title = Title
        self.Author = Author
        self.Era = Era
        self.Publisher = Publisher
        self.Target = Target
        self.Genre = Genre
        self.Type = Type
    
    def get_File(self):
        return self.File

    def get_Title(self):
        return self.Title

    def get_Author(self):
        return self.Author
    
    def get_Era(self):
        return self.Era

    def get_Publisher(self):
        return self.Publisher
    
    def get_Target(self):
        return self.Target

    def get_Genre(self):
        return self.Genre
    
    def get_Type(self):
        return self.Type

    

class MainComic(Comic):
    def __init__(self, File, Title, Author, Era, Publisher, Target, Genre, Type, PageCount, FrameRanges, CharacterInstances, BorderRates, FeaturedCharacterCount, FeatureRank_FeaturedCharacterInstance, SBDComicRanking):
        super().__init__(File, Title, Author, Era, Publisher, Target, Genre, Type)
        self.PageCount = PageCount
        self.FrameRanges = FrameRanges
        self.CharacterInstances = CharacterInstances
        self.BorderRates = BorderRates
        self.FeaturedCharacterCount = FeaturedCharacterCount
        self.FeatureRank_FeaturedCharacterInstance = FeatureRank_FeaturedCharacterInstance
        self.SBDComicRanking = SBDComicRanking
    
    def get_PageCount(self):
        return self.PageCount

    def set_PageCount(self, PageCount):
        self.PageCount = PageCount

    def get_FrameRanges(self):
        return self.FrameRanges

    def set_FrameRanges(self, FrameRanges):
        self.FrameRanges = FrameRanges

    def get_CharacterInstances(self):
        return self.CharacterInstances
    
    def set_CharacterInstances(self, CharacterInstances):
        self.CharacterInstances = CharacterInstances

    def get_BorderRates(self):
        return self.BorderRates

    def set_BorderRates(self, BorderRates):
        self.BorderRates = BorderRates

    def get_FeaturedCharacterCount(self):
        return self.FeaturedCharacterCount

    def set_FeaturedCharacterCount(self, FeaturedCharacterCount):
        self.FeaturedCharacterCount = FeaturedCharacterCount

    def get_FeatureRank_FeaturedCharacterInstance(self):
        return self.FeatureRank_FeaturedCharacterInstance
    
    def set_FeatureRank_FeaturedCharacterInstance(self, FeatureRank_FeaturedCharacterInstance):
        self.FeatureRank_FeaturedCharacterInstance = FeatureRank_FeaturedCharacterInstance

    def get_SBDComicRanking(self):
        return self.SBDComicRanking

    def set_SBDComicRanking(self, SBDComicRanking):
        self.SBDComicRanking = SBDComicRanking



class SubComic(Comic):
    def __init__(self, File, Title, Author, Era, Publisher, Target, Genre, Type, Distance):
        super().__init__(File, Title, Author, Era, Publisher, Target, Genre, Type)
        self.Distance = Distance
    
    def get_Distance(self):
        return self.Distance
    


class Character:
    def __init__(self, Id, Name, CharacterRates):
        self.Id = Id
        self.Name = Name
        self.CharacterRates = CharacterRates
    
    def get_Id(self):
        return self.Id

    def get_Name(self):
        return self.Name
    
    def get_CharacterRates(self):
        return self.CharacterRates

    def set_CharacterRates(self, CharacterRates):
        self.CharacterRates = CharacterRates
    

class FeaturedCharacter(Character):
    def __init__(self, Id, Name, CharacterRates, FeaturedCharacterRates):
        super().__init__(Id, Name, CharacterRates)
        self.FeaturedCharacterRates = FeaturedCharacterRates
    
    def get_FeaturedCharacterRates(self):
        return self.FeaturedCharacterRates 


    

