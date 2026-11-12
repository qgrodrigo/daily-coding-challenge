function generateSignature(name, title, company) {

    let signature = '';
    let prefix = '';

    console.log(name[0].toLowerCase().charCodeAt(0))

    if (name[0].toLowerCase().charCodeAt(0) >= 97 && name[0].toLowerCase().charCodeAt(0) <= 105){
        prefix = '>>';
    }

    if (name[0].toLowerCase().charCodeAt(0) >= 106 && name[0].toLowerCase().charCodeAt(0) <= 114){
        prefix = '--';
    }

    if (name[0].toLowerCase().charCodeAt(0) >= 115 && name[0].toLowerCase().charCodeAt(0) <= 122){
        prefix = '::';
    }

    signature = prefix + name + ", " + title + " at " + company;

    console.log(signature);

    return signature;
}

//Tests:
generateSignature("Quinn Waverly", "Founder and CEO", "TechCo") //should return "--Quinn Waverly, Founder and CEO at TechCo".
generateSignature("Alice Reed", "Engineer", "TechCo") //should return ">>Alice Reed, Engineer at TechCo".
generateSignature("Tina Vaughn", "Developer", "example.com") //should return "::Tina Vaughn, Developer at example.com".
generateSignature("B. B.", "Product Tester", "AcmeCorp") //should return ">>B. B., Product Tester at AcmeCorp".
generateSignature("windstorm", "Cloud Architect", "Atmospheronics") //should return "::windstorm, Cloud Architect at Atmospheronics".