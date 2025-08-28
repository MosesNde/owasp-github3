 import * as UserBackend from "./backend/UserBackend";
 import * as OrganizationBackend from "./backend/OrganizationBackend";
 import * as Setting from "./Setting";
import {LinkOutlined} from "@ant-design/icons";
 import i18next from "i18next";
 import CropperDiv from "./CropperDiv.js";
 import * as ApplicationBackend from "./backend/ApplicationBackend";
             {Setting.getLabel(i18next.t("general:Avatar"), i18next.t("general:Avatar - Tooltip"))} :
           </Col>
           <Col span={22} >
            <Row style={{marginTop: "20px"}} >
              <Col style={{marginTop: "5px"}} span={(Setting.isMobile()) ? 22 : 2}>
                {i18next.t("general:URL")}:
              </Col>
              <Col span={22} >
                <Input prefix={<LinkOutlined />} value={this.state.user.avatar} onChange={e => {
                  this.updateUserField("avatar", e.target.value);
                }} />
              </Col>
            </Row>
             <Row style={{marginTop: "20px"}} >
               <Col style={{marginTop: "5px"}} span={(Setting.isMobile()) ? 22 : 2}>
                 {i18next.t("general:Preview")}: