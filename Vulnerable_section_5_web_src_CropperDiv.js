 // See the License for the specific language governing permissions and
 // limitations under the License.
 
import React, {useState} from "react";
 import Cropper from "react-cropper";
 import "cropperjs/dist/cropper.css";
 import * as Setting from "./Setting";
import {Button, Col, Modal, Row} from "antd";
 import i18next from "i18next";
 import * as ResourceBackend from "./backend/ResourceBackend";
 
 export const CropperDiv = (props) => {
   const [image, setImage] = useState("");
   const [cropper, setCropper] = useState();
  const [visible, setVisible] = React.useState(false);
  const [confirmLoading, setConfirmLoading] = React.useState(false);
   const {title} = props;
   const {user} = props;
   const {buttonText} = props;
       ResourceBackend.uploadResource(user.owner, user.name, "avatar", "CropperDiv", fullFilePath, blob)
         .then((res) => {
           if (res.status === "ok") {
            window.location.href = "/account";
           } else {
             Setting.showMessage("error", res.msg);
           }
     uploadButton.click();
   };
 
   return (
     <div>
       <Button type="default" onClick={showModal}>
           [<Button block key="submit" type="primary" onClick={handleOk}>{i18next.t("user:Set new profile picture")}</Button>]
         }
       >
        <Col style={{margin: "0px auto 40px auto", width: 1000, height: 300}}>
           <Row style={{width: "100%", marginBottom: "20px"}}>
             <input style={{display: "none"}} ref={input => uploadButton = input} type="file" accept="image/*" onChange={onChange} />
             <Button block onClick={selectFile}>{i18next.t("user:Select a photo...")}</Button>
           </Row>
           <Cropper
             style={{height: "100%"}}