import logging
import webbrowser


class AmazonSDEJobApplication:
    logging.info("Job application for the position of Software Development Engineer @ Amazon")

    def __init__(self, name, location, email, contact_number):
        self.personalInfo = dict()
        self.personalInfo["Name: "] = name
        self.personalInfo["CurrentLocation: "] = location
        self.personalInfo["Email: "] = email
        self.personalInfo["ContactNumber: "] = contact_number

    def build_resume(self):
        print("Creating my profile for your reference")
        experience = self.get_experience()
        edu_details = self.get_educational_details()
        social_media_contact = self.get_social_media_contacts()
        resume = open("JAYENDRAN_RESUME.txt", "w")
        resume.write(str(self.personalInfo))
        resume.write(str(experience))
        resume.write(str(edu_details))
        resume.write(str(social_media_contact))
        resume.close()
        self.say_thanks()

    @classmethod
    def view_my_resume(cls):
        logging.info("Jayendran resume is loading...")
        webbrowser.open("JAYENDRAN_RESUME.txt")

    @classmethod
    def get_experience(cls):
        experience = list()
        experience.append("Currently working as a Software Developer at Zoho Corporation, Chennai")
        experience.append("Did my QAT internship in Amazon Appstore(Fire TV and Fire Tablets)team at"
                          " Amazon Development Centre, Chennai")
        experience.append("Also did an internship of 3 months in Data Analytics and Machine Learning domain at "
                          "Walinns Analytics India Pvt Ltd,Tidel park:Coimbatore")
        return experience

    @classmethod
    def get_educational_details(cls):
        edu_details = dict()
        edu_details["Course"] = "B.Tech Information Technology"
        edu_details["Batch"] = "2015-2019"
        edu_details["Favorite Subjects"] = "Data structures & Algorithms, Mathematics, AI & ML"
        return edu_details

    @classmethod
    def get_social_media_contacts(cls):
        social_media_contacts = dict()
        social_media_contacts["LinkedIn"] = "https://www.linkedin.com/in/jayendran-s-194b66122/"
        social_media_contacts["GitHub"] = "https://github.com/jaijaish98"
        return social_media_contacts

    def say_thanks(self):
        print("I'm eagerly waiting for your response to have a discussion with you regarding this opportunity")
        print("Best Regards,")
        print("{}".format(self.personalInfo["Name: "]))
        print("{}".format(self.personalInfo["ContactNumber: "]))


if __name__ == '__main__':
    language = "Python 3.X"
    print("Programming language here I used is {}.".format(language))
    name = "Jayendran S"
    current_location = "Chennai"
    email = "jaijaish98@gmail.com"
    contact_number = "(+91) 996 557 2470"
    job_application = AmazonSDEJobApplication(name, current_location, email, contact_number)
    job_application.build_resume()
    job_application.view_my_resume()

