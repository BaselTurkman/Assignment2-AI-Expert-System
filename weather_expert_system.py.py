class WeatherExpertSystem:
    def __init__(self):
        self.tomorrow = {}
        self.today = {}
        self.facts = {}

    def _get_valid_response(self,option1, option2, question):
        while True:
            user_input = input(f"What is the {question} today? ({option1} / {option2}) ? : ").lower()
            if user_input == option1 or user_input == option2:
                return user_input
            else:
                print(f"{user_input} is not a valid answer. Please try again.")

    def _get_valid_degree(self, entity, attribute):
        while True:
            try:
                user_input = float(input(f"To what degree do you believe the {entity} is {attribute}? Enter a numeric certainty between O and 1.0 inclusive. "))
                if 0<=user_input<=1:
                    return user_input
                print(f"{user_input} is not a valid answer. Please try again.")
            except:
                print("Please enter a numeric certainty between O and 1.0 inclusive.")
    def _ask_about_weather(self):
        weather = self._get_valid_response("rain","dry","Weather")
        #applying rules 1 and 2
        self.today[weather]  = 1
        self.tomorrow[weather] = 0.5

    def _ask_about_rainfall(self):
        rainfall = self._get_valid_response("low","high","rainfall")
        degree = self._get_valid_degree("rainfall", rainfall)
        self.facts["rainfall is low"] = degree
        #apply rule 3
        if "rain" in self.today and rainfall =="low":
            print("applying rule 3")
            degree = min(self.today.get("rain"),degree)*0.6
            self.tomorrow["dry"] = degree
            
    def _ask_about_temperature(self):
        temperature = self._get_valid_response("cold","warm","Temperature")
        degree = self._get_valid_degree("Temperature", temperature)
        self.facts[f"temperature is {temperature}"] = degree
        #apply rule 4
        if "rain" in self.today and "rainfall is low" in self.facts and temperature =="cold":
            print("applying rule 4")
            if "dry" in self.tomorrow:
                degree= min(self.today.get("rain"),self.facts.get("rainfall is low"),degree)*0.7
                self.tomorrow["dry"]=self._update_certainty_factors(self.tomorrow.get("dry"),degree)
            else:
                degree= min(self.today.get("rain"),self.facts.get("rainfall is low"),degree)*0.7
                self.tomorrow["dry"]=degree

        #apply rule 5
        if "dry" in self.today and temperature =="warm":
            print("Applying rule 5")
            if "rain" in self.tomorrow:
                degree= min( self.today.get("dry"),degree)*0.65
                self.tomorrow["rain"]=self._update_certainty_factors(self.tomorrow.get("rain"),degree)
            else:
                degree= min( self.today.get("dry"),degree)*0.65
                self.tomorrow["rain"]=degree

    def _ask_about_sky(self):
        sky = self._get_valid_response("overcast","clear","Sky")
        degree = self._get_valid_degree("Sky", sky)
        self.facts[f"sky is {sky}"] = degree
        #apply rule 6
        if "dry" in self.today and "temperature is warm" in self.facts and sky =="overcast":
            print("Applying rule 6")
            if "rain" in self.tomorrow:
                degree = min(self.today.get("dry"),self.facts.get("temperature is warm"),degree)*0.55
                self.tomorrow["rain"]=self._update_certainty_factors(self.tomorrow.get("rain"),degree)
            else:
                degree = min(self.today.get("dry"),self.facts.get("temperature is warm"),degree)*0.55
                self.tomorrow["rainfall is low"]=degree 
        
    def _update_certainty_factors(self,cf1,cf2):
        if cf1>0 and cf2>0:
            return round(cf1+cf2*(1-cf1),2)
        elif cf1<0 or cf2<0:
            return round((cf1+cf2)/1-min(abs(cf1),abs(cf2)),2)
        elif cf1<0 and cf2<0:
            return round(cf1+cf2*(1+cf1),2)
        
    def predict_weather(self):
        self._ask_about_weather()
        self._ask_about_rainfall()
        self._ask_about_temperature()
        self._ask_about_sky()
        print("Tomorrow is: ",self.tomorrow)


def main():
    test = WeatherExpertSystem()
    test.predict_weather()

if __name__ == "__main__":
    main()
