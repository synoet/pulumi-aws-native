// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./crl";
export * from "./getCRL";
export * from "./getProfile";
export * from "./getTrustAnchor";
export * from "./profile";
export * from "./trustAnchor";

// Export enums:
export * from "../types/enums/rolesanywhere";

// Import resources to register:
import { CRL } from "./crl";
import { Profile } from "./profile";
import { TrustAnchor } from "./trustAnchor";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:rolesanywhere:CRL":
                return new CRL(name, <any>undefined, { urn })
            case "aws-native:rolesanywhere:Profile":
                return new Profile(name, <any>undefined, { urn })
            case "aws-native:rolesanywhere:TrustAnchor":
                return new TrustAnchor(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "rolesanywhere", _module)
