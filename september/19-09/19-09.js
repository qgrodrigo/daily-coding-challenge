function numberOfPhotos(photoSizeMb, hardDriveSizeGb) {

    let photo = (hardDriveSizeGb * 1000) / photoSizeMb
    console.log(photo);

    return Math.floor(photo);
}