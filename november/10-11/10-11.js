function getExtension(filename) {

    let fileParts = filename.split('.');
    let extension = 'none';

    if (filename.includes('.')){
        extension = fileParts[fileParts.length -1];
    }

    if (extension == ''){
        extension = 'none';
    }

    //console.log(fileParts);
    console.log(extension);

    return extension;
}

//Tests:
getExtension("document.txt") //should return "txt".
getExtension("README") //should return "none".
getExtension("image.PNG") //should return "PNG".
getExtension(".gitignore") //should return "gitignore".
getExtension("archive.tar.gz") //should return "gz".
getExtension("final.draft.") //should return "none".