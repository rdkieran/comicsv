# comicsv (Comic CSV)

Developed to generate a list of embed links and basic HTML files for comic pages stored on on Google Drive.
readme under construction

#### google app script excerpt for getting file info
```
// replace your-folder below with the folder for which you want a listing
function listFolderContents() {
  var foldername = 'your-folder';
  var folderlisting = 'listing of folder ' + foldername;
  
  var folders = DriveApp.getFoldersByName(foldername)
  var folder = folders.next();
  var contents = folder.getFiles();
  
  var ss = SpreadsheetApp.create(folderlisting);
  var sheet = ss.getActiveSheet();
  sheet.appendRow( ['name', 'link'] );
  
  var file;
  var name;
  var link;
  var row;
  while(contents.hasNext()) {
    file = contents.next();
    name = file.getName();
    link = file.getUrl();
    sheet.appendRow( [name, link] );     
  }  
};
```
&mdash; [List Google Drive Folder File Names and URLs to a Google Sheet](https://www.acrosswalls.org/ortext-datalinks/list-google-drive-folder-file-names-urls/)

#### resulting CSV from script
```
name,link
00 hourlies 2022.clip,https://drive.google.com/file/d/1I5tB-ekcmFL2lO3nzf9Fiv1dpoFuqlCJ/view?usp=drivesdk
hourlies 22 14.png,https://drive.google.com/file/d/1Eu3WsHdLe9xiPQW7MLZaq0ch22eCOWA7/view?usp=drivesdk
hourlies 22 13.png,https://drive.google.com/file/d/1rh2EvcCPkJFsQtBwofd36_wk07KJTzLO/view?usp=drivesdk
hourlies 22 12.png,https://drive.google.com/file/d/19o87Vltp2kdwk13zuZsLasEFfkdAIJIx/view?usp=drivesdk
hourlies 22 11.png,https://drive.google.com/file/d/1kvBxFucUYgwX7K5F5E62yjOJM0LoSaP4/view?usp=drivesdk
hourlies 22 10.png,https://drive.google.com/file/d/1FDwPeXubtmtjTX09SzhU2K2EpboPWoQx/view?usp=drivesdk
hourlies 22 09.png,https://drive.google.com/file/d/1akH_4llx7us90dCEx9dgPR8hN_ipRbxc/view?usp=drivesdk
hourlies 22 08.png,https://drive.google.com/file/d/1-PML72h_76kTlzzatsMN8rinXsmOKtPv/view?usp=drivesdk
hourlies 22 07.png,https://drive.google.com/file/d/1_zVfPub9wOuOqEIwCu3N7d_L0ey9AIOe/view?usp=drivesdk
hourlies 22 06.png,https://drive.google.com/file/d/1yghAIG2CYDhilGNrSIPVDnXAtCr2eK-D/view?usp=drivesdk
hourlies 22 05.png,https://drive.google.com/file/d/1uTFzWk_kKd99oBzb0Iz9aAAThZRcWGSO/view?usp=drivesdk
hourlies 22 04.png,https://drive.google.com/file/d/1Tl7YBJ70PKtkOq2QoTOGYZN7i-B-dxq3/view?usp=drivesdk
hourlies 22 03.png,https://drive.google.com/file/d/1nxlObLZohQO9075nkcEpdvbQ2nH67IrL/view?usp=drivesdk
hourlies 22 02.png,https://drive.google.com/file/d/1k2-fdwRLBmxSvbDS52o1cZ5-Yo21j2Q5/view?usp=drivesdk
hourlies 22 01.png,https://drive.google.com/file/d/1Ri0TlAsh5ijfA_w5KnstOf2R96E3x3Uy/view?usp=drivesdk
```
&mdash; 'listing of folder hourlies-22 - Sheet1.csv'

#### .txt file with listed data, processed from CSV, with Google Drive share links formatted properly
```
rat boy diaries,01,https://drive.google.com/uc?export=view&id=1Ri0TlAsh5ijfA_w5KnstOf2R96E3x3Uy
rat boy diaries,02,https://drive.google.com/uc?export=view&id=1k2-fdwRLBmxSvbDS52o1cZ5-Yo21j2Q5
rat boy diaries,03,https://drive.google.com/uc?export=view&id=1nxlObLZohQO9075nkcEpdvbQ2nH67IrL
rat boy diaries,04,https://drive.google.com/uc?export=view&id=1Tl7YBJ70PKtkOq2QoTOGYZN7i-B-dxq3
rat boy diaries,05,https://drive.google.com/uc?export=view&id=1uTFzWk_kKd99oBzb0Iz9aAAThZRcWGSO
rat boy diaries,06,https://drive.google.com/uc?export=view&id=1yghAIG2CYDhilGNrSIPVDnXAtCr2eK-D
rat boy diaries,07,https://drive.google.com/uc?export=view&id=1_zVfPub9wOuOqEIwCu3N7d_L0ey9AIOe
rat boy diaries,08,https://drive.google.com/uc?export=view&id=1-PML72h_76kTlzzatsMN8rinXsmOKtPv
rat boy diaries,09,https://drive.google.com/uc?export=view&id=1akH_4llx7us90dCEx9dgPR8hN_ipRbxc
rat boy diaries,10,https://drive.google.com/uc?export=view&id=1FDwPeXubtmtjTX09SzhU2K2EpboPWoQx
rat boy diaries,11,https://drive.google.com/uc?export=view&id=1kvBxFucUYgwX7K5F5E62yjOJM0LoSaP4
rat boy diaries,12,https://drive.google.com/uc?export=view&id=19o87Vltp2kdwk13zuZsLasEFfkdAIJIx
rat boy diaries,13,https://drive.google.com/uc?export=view&id=1rh2EvcCPkJFsQtBwofd36_wk07KJTzLO
rat boy diaries,14,https://drive.google.com/uc?export=view&id=1Eu3WsHdLe9xiPQW7MLZaq0ch22eCOWA7
```
&mdash; 'rat-boy-diaries\rat-boy-diaries.txt'

#### template HTML file
```
<!DOCTYPE html>
<html>
    <head>
        <title>[[PROJECT NAME]], Page [[PAGE NUMBER]]</title>
    </head>
    <body>
        <img src="[[SOURCE]]" alt="[[ALT]]">
    </body>
</html>
```
&mdash; 'convert-to-html\template.html'

#### template with sample data inserted
```
<!DOCTYPE html>
<html>
    <head>
        <title>Rat boy diaries, Page page 1</title>
    </head>
    <body>
        <img src="https://drive.google.com/uc?export=view&id=1Ri0TlAsh5ijfA_w5KnstOf2R96E3x3Uy" alt="rat boy diaries, page 1">
    </body>
</html>
```
&mdash; 'rat-boy-diaries\01.html'
