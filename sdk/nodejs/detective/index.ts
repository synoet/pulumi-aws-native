// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetGraphArgs, GetGraphResult, GetGraphOutputArgs } from "./getGraph";
export const getGraph: typeof import("./getGraph").getGraph = null as any;
export const getGraphOutput: typeof import("./getGraph").getGraphOutput = null as any;
utilities.lazyLoad(exports, ["getGraph","getGraphOutput"], () => require("./getGraph"));

export { GetMemberInvitationArgs, GetMemberInvitationResult, GetMemberInvitationOutputArgs } from "./getMemberInvitation";
export const getMemberInvitation: typeof import("./getMemberInvitation").getMemberInvitation = null as any;
export const getMemberInvitationOutput: typeof import("./getMemberInvitation").getMemberInvitationOutput = null as any;
utilities.lazyLoad(exports, ["getMemberInvitation","getMemberInvitationOutput"], () => require("./getMemberInvitation"));

export { GetOrganizationAdminArgs, GetOrganizationAdminResult, GetOrganizationAdminOutputArgs } from "./getOrganizationAdmin";
export const getOrganizationAdmin: typeof import("./getOrganizationAdmin").getOrganizationAdmin = null as any;
export const getOrganizationAdminOutput: typeof import("./getOrganizationAdmin").getOrganizationAdminOutput = null as any;
utilities.lazyLoad(exports, ["getOrganizationAdmin","getOrganizationAdminOutput"], () => require("./getOrganizationAdmin"));

export { GraphArgs } from "./graph";
export type Graph = import("./graph").Graph;
export const Graph: typeof import("./graph").Graph = null as any;
utilities.lazyLoad(exports, ["Graph"], () => require("./graph"));

export { MemberInvitationArgs } from "./memberInvitation";
export type MemberInvitation = import("./memberInvitation").MemberInvitation;
export const MemberInvitation: typeof import("./memberInvitation").MemberInvitation = null as any;
utilities.lazyLoad(exports, ["MemberInvitation"], () => require("./memberInvitation"));

export { OrganizationAdminArgs } from "./organizationAdmin";
export type OrganizationAdmin = import("./organizationAdmin").OrganizationAdmin;
export const OrganizationAdmin: typeof import("./organizationAdmin").OrganizationAdmin = null as any;
utilities.lazyLoad(exports, ["OrganizationAdmin"], () => require("./organizationAdmin"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:detective:Graph":
                return new Graph(name, <any>undefined, { urn })
            case "aws-native:detective:MemberInvitation":
                return new MemberInvitation(name, <any>undefined, { urn })
            case "aws-native:detective:OrganizationAdmin":
                return new OrganizationAdmin(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "detective", _module)
