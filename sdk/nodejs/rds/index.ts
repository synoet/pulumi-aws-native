// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./dbproxy";
export * from "./dbproxyEndpoint";
export * from "./dbproxyTargetGroup";
export * from "./globalCluster";

// Export enums:
export * from "../types/enums/rds";

// Import resources to register:
import { DBProxy } from "./dbproxy";
import { DBProxyEndpoint } from "./dbproxyEndpoint";
import { DBProxyTargetGroup } from "./dbproxyTargetGroup";
import { GlobalCluster } from "./globalCluster";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:rds:DBProxy":
                return new DBProxy(name, <any>undefined, { urn })
            case "aws-native:rds:DBProxyEndpoint":
                return new DBProxyEndpoint(name, <any>undefined, { urn })
            case "aws-native:rds:DBProxyTargetGroup":
                return new DBProxyTargetGroup(name, <any>undefined, { urn })
            case "aws-native:rds:GlobalCluster":
                return new GlobalCluster(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "rds", _module)
