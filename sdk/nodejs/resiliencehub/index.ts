// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { AppArgs } from "./app";
export type App = import("./app").App;
export const App: typeof import("./app").App = null as any;
utilities.lazyLoad(exports, ["App"], () => require("./app"));

export { GetAppArgs, GetAppResult, GetAppOutputArgs } from "./getApp";
export const getApp: typeof import("./getApp").getApp = null as any;
export const getAppOutput: typeof import("./getApp").getAppOutput = null as any;
utilities.lazyLoad(exports, ["getApp","getAppOutput"], () => require("./getApp"));

export { GetResiliencyPolicyArgs, GetResiliencyPolicyResult, GetResiliencyPolicyOutputArgs } from "./getResiliencyPolicy";
export const getResiliencyPolicy: typeof import("./getResiliencyPolicy").getResiliencyPolicy = null as any;
export const getResiliencyPolicyOutput: typeof import("./getResiliencyPolicy").getResiliencyPolicyOutput = null as any;
utilities.lazyLoad(exports, ["getResiliencyPolicy","getResiliencyPolicyOutput"], () => require("./getResiliencyPolicy"));

export { ResiliencyPolicyArgs } from "./resiliencyPolicy";
export type ResiliencyPolicy = import("./resiliencyPolicy").ResiliencyPolicy;
export const ResiliencyPolicy: typeof import("./resiliencyPolicy").ResiliencyPolicy = null as any;
utilities.lazyLoad(exports, ["ResiliencyPolicy"], () => require("./resiliencyPolicy"));


// Export enums:
export * from "../types/enums/resiliencehub";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:resiliencehub:App":
                return new App(name, <any>undefined, { urn })
            case "aws-native:resiliencehub:ResiliencyPolicy":
                return new ResiliencyPolicy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "resiliencehub", _module)
