// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetResourceShareArgs, GetResourceShareResult, GetResourceShareOutputArgs } from "./getResourceShare";
export const getResourceShare: typeof import("./getResourceShare").getResourceShare = null as any;
export const getResourceShareOutput: typeof import("./getResourceShare").getResourceShareOutput = null as any;
utilities.lazyLoad(exports, ["getResourceShare","getResourceShareOutput"], () => require("./getResourceShare"));

export { ResourceShareArgs } from "./resourceShare";
export type ResourceShare = import("./resourceShare").ResourceShare;
export const ResourceShare: typeof import("./resourceShare").ResourceShare = null as any;
utilities.lazyLoad(exports, ["ResourceShare"], () => require("./resourceShare"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:ram:ResourceShare":
                return new ResourceShare(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "ram", _module)
