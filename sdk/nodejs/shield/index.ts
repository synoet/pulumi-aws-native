// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { DrtAccessArgs } from "./drtAccess";
export type DrtAccess = import("./drtAccess").DrtAccess;
export const DrtAccess: typeof import("./drtAccess").DrtAccess = null as any;
utilities.lazyLoad(exports, ["DrtAccess"], () => require("./drtAccess"));

export { GetDrtAccessArgs, GetDrtAccessResult, GetDrtAccessOutputArgs } from "./getDrtAccess";
export const getDrtAccess: typeof import("./getDrtAccess").getDrtAccess = null as any;
export const getDrtAccessOutput: typeof import("./getDrtAccess").getDrtAccessOutput = null as any;
utilities.lazyLoad(exports, ["getDrtAccess","getDrtAccessOutput"], () => require("./getDrtAccess"));

export { GetProactiveEngagementArgs, GetProactiveEngagementResult, GetProactiveEngagementOutputArgs } from "./getProactiveEngagement";
export const getProactiveEngagement: typeof import("./getProactiveEngagement").getProactiveEngagement = null as any;
export const getProactiveEngagementOutput: typeof import("./getProactiveEngagement").getProactiveEngagementOutput = null as any;
utilities.lazyLoad(exports, ["getProactiveEngagement","getProactiveEngagementOutput"], () => require("./getProactiveEngagement"));

export { GetProtectionArgs, GetProtectionResult, GetProtectionOutputArgs } from "./getProtection";
export const getProtection: typeof import("./getProtection").getProtection = null as any;
export const getProtectionOutput: typeof import("./getProtection").getProtectionOutput = null as any;
utilities.lazyLoad(exports, ["getProtection","getProtectionOutput"], () => require("./getProtection"));

export { GetProtectionGroupArgs, GetProtectionGroupResult, GetProtectionGroupOutputArgs } from "./getProtectionGroup";
export const getProtectionGroup: typeof import("./getProtectionGroup").getProtectionGroup = null as any;
export const getProtectionGroupOutput: typeof import("./getProtectionGroup").getProtectionGroupOutput = null as any;
utilities.lazyLoad(exports, ["getProtectionGroup","getProtectionGroupOutput"], () => require("./getProtectionGroup"));

export { ProactiveEngagementArgs } from "./proactiveEngagement";
export type ProactiveEngagement = import("./proactiveEngagement").ProactiveEngagement;
export const ProactiveEngagement: typeof import("./proactiveEngagement").ProactiveEngagement = null as any;
utilities.lazyLoad(exports, ["ProactiveEngagement"], () => require("./proactiveEngagement"));

export { ProtectionArgs } from "./protection";
export type Protection = import("./protection").Protection;
export const Protection: typeof import("./protection").Protection = null as any;
utilities.lazyLoad(exports, ["Protection"], () => require("./protection"));

export { ProtectionGroupArgs } from "./protectionGroup";
export type ProtectionGroup = import("./protectionGroup").ProtectionGroup;
export const ProtectionGroup: typeof import("./protectionGroup").ProtectionGroup = null as any;
utilities.lazyLoad(exports, ["ProtectionGroup"], () => require("./protectionGroup"));


// Export enums:
export * from "../types/enums/shield";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:shield:DrtAccess":
                return new DrtAccess(name, <any>undefined, { urn })
            case "aws-native:shield:ProactiveEngagement":
                return new ProactiveEngagement(name, <any>undefined, { urn })
            case "aws-native:shield:Protection":
                return new Protection(name, <any>undefined, { urn })
            case "aws-native:shield:ProtectionGroup":
                return new ProtectionGroup(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "shield", _module)
