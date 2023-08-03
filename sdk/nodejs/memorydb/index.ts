// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { AclArgs } from "./acl";
export type Acl = import("./acl").Acl;
export const Acl: typeof import("./acl").Acl = null as any;
utilities.lazyLoad(exports, ["Acl"], () => require("./acl"));

export { ClusterArgs } from "./cluster";
export type Cluster = import("./cluster").Cluster;
export const Cluster: typeof import("./cluster").Cluster = null as any;
utilities.lazyLoad(exports, ["Cluster"], () => require("./cluster"));

export { GetAclArgs, GetAclResult, GetAclOutputArgs } from "./getAcl";
export const getAcl: typeof import("./getAcl").getAcl = null as any;
export const getAclOutput: typeof import("./getAcl").getAclOutput = null as any;
utilities.lazyLoad(exports, ["getAcl","getAclOutput"], () => require("./getAcl"));

export { GetClusterArgs, GetClusterResult, GetClusterOutputArgs } from "./getCluster";
export const getCluster: typeof import("./getCluster").getCluster = null as any;
export const getClusterOutput: typeof import("./getCluster").getClusterOutput = null as any;
utilities.lazyLoad(exports, ["getCluster","getClusterOutput"], () => require("./getCluster"));

export { GetParameterGroupArgs, GetParameterGroupResult, GetParameterGroupOutputArgs } from "./getParameterGroup";
export const getParameterGroup: typeof import("./getParameterGroup").getParameterGroup = null as any;
export const getParameterGroupOutput: typeof import("./getParameterGroup").getParameterGroupOutput = null as any;
utilities.lazyLoad(exports, ["getParameterGroup","getParameterGroupOutput"], () => require("./getParameterGroup"));

export { GetSubnetGroupArgs, GetSubnetGroupResult, GetSubnetGroupOutputArgs } from "./getSubnetGroup";
export const getSubnetGroup: typeof import("./getSubnetGroup").getSubnetGroup = null as any;
export const getSubnetGroupOutput: typeof import("./getSubnetGroup").getSubnetGroupOutput = null as any;
utilities.lazyLoad(exports, ["getSubnetGroup","getSubnetGroupOutput"], () => require("./getSubnetGroup"));

export { GetUserArgs, GetUserResult, GetUserOutputArgs } from "./getUser";
export const getUser: typeof import("./getUser").getUser = null as any;
export const getUserOutput: typeof import("./getUser").getUserOutput = null as any;
utilities.lazyLoad(exports, ["getUser","getUserOutput"], () => require("./getUser"));

export { ParameterGroupArgs } from "./parameterGroup";
export type ParameterGroup = import("./parameterGroup").ParameterGroup;
export const ParameterGroup: typeof import("./parameterGroup").ParameterGroup = null as any;
utilities.lazyLoad(exports, ["ParameterGroup"], () => require("./parameterGroup"));

export { SubnetGroupArgs } from "./subnetGroup";
export type SubnetGroup = import("./subnetGroup").SubnetGroup;
export const SubnetGroup: typeof import("./subnetGroup").SubnetGroup = null as any;
utilities.lazyLoad(exports, ["SubnetGroup"], () => require("./subnetGroup"));

export { UserArgs } from "./user";
export type User = import("./user").User;
export const User: typeof import("./user").User = null as any;
utilities.lazyLoad(exports, ["User"], () => require("./user"));


// Export enums:
export * from "../types/enums/memorydb";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:memorydb:Acl":
                return new Acl(name, <any>undefined, { urn })
            case "aws-native:memorydb:Cluster":
                return new Cluster(name, <any>undefined, { urn })
            case "aws-native:memorydb:ParameterGroup":
                return new ParameterGroup(name, <any>undefined, { urn })
            case "aws-native:memorydb:SubnetGroup":
                return new SubnetGroup(name, <any>undefined, { urn })
            case "aws-native:memorydb:User":
                return new User(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "memorydb", _module)
