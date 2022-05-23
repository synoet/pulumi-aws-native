// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./connectAttachment";
export * from "./connectPeer";
export * from "./coreNetwork";
export * from "./customerGatewayAssociation";
export * from "./device";
export * from "./getConnectAttachment";
export * from "./getConnectPeer";
export * from "./getCoreNetwork";
export * from "./getDevice";
export * from "./getGlobalNetwork";
export * from "./getLink";
export * from "./getSite";
export * from "./getSiteToSiteVpnAttachment";
export * from "./getVpcAttachment";
export * from "./globalNetwork";
export * from "./link";
export * from "./linkAssociation";
export * from "./site";
export * from "./siteToSiteVpnAttachment";
export * from "./transitGatewayRegistration";
export * from "./vpcAttachment";

// Import resources to register:
import { ConnectAttachment } from "./connectAttachment";
import { ConnectPeer } from "./connectPeer";
import { CoreNetwork } from "./coreNetwork";
import { CustomerGatewayAssociation } from "./customerGatewayAssociation";
import { Device } from "./device";
import { GlobalNetwork } from "./globalNetwork";
import { Link } from "./link";
import { LinkAssociation } from "./linkAssociation";
import { Site } from "./site";
import { SiteToSiteVpnAttachment } from "./siteToSiteVpnAttachment";
import { TransitGatewayRegistration } from "./transitGatewayRegistration";
import { VpcAttachment } from "./vpcAttachment";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:networkmanager:ConnectAttachment":
                return new ConnectAttachment(name, <any>undefined, { urn })
            case "aws-native:networkmanager:ConnectPeer":
                return new ConnectPeer(name, <any>undefined, { urn })
            case "aws-native:networkmanager:CoreNetwork":
                return new CoreNetwork(name, <any>undefined, { urn })
            case "aws-native:networkmanager:CustomerGatewayAssociation":
                return new CustomerGatewayAssociation(name, <any>undefined, { urn })
            case "aws-native:networkmanager:Device":
                return new Device(name, <any>undefined, { urn })
            case "aws-native:networkmanager:GlobalNetwork":
                return new GlobalNetwork(name, <any>undefined, { urn })
            case "aws-native:networkmanager:Link":
                return new Link(name, <any>undefined, { urn })
            case "aws-native:networkmanager:LinkAssociation":
                return new LinkAssociation(name, <any>undefined, { urn })
            case "aws-native:networkmanager:Site":
                return new Site(name, <any>undefined, { urn })
            case "aws-native:networkmanager:SiteToSiteVpnAttachment":
                return new SiteToSiteVpnAttachment(name, <any>undefined, { urn })
            case "aws-native:networkmanager:TransitGatewayRegistration":
                return new TransitGatewayRegistration(name, <any>undefined, { urn })
            case "aws-native:networkmanager:VpcAttachment":
                return new VpcAttachment(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "networkmanager", _module)
