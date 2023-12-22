// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SageMaker::Domain
 */
export function getDomain(args: GetDomainArgs, opts?: pulumi.InvokeOptions): Promise<GetDomainResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:sagemaker:getDomain", {
        "domainId": args.domainId,
    }, opts);
}

export interface GetDomainArgs {
    /**
     * The domain name.
     */
    domainId: string;
}

export interface GetDomainResult {
    /**
     * Specifies the VPC used for non-EFS traffic. The default value is PublicInternetOnly.
     */
    readonly appNetworkAccessType?: enums.sagemaker.DomainAppNetworkAccessType;
    /**
     * The entity that creates and manages the required security groups for inter-app communication in VPCOnly mode. Required when CreateDomain.AppNetworkAccessType is VPCOnly and DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn is provided.
     */
    readonly appSecurityGroupManagement?: enums.sagemaker.DomainAppSecurityGroupManagement;
    /**
     * The default space settings.
     */
    readonly defaultSpaceSettings?: outputs.sagemaker.DomainDefaultSpaceSettings;
    /**
     * The default user settings.
     */
    readonly defaultUserSettings?: outputs.sagemaker.DomainUserSettings;
    /**
     * The Amazon Resource Name (ARN) of the created domain.
     */
    readonly domainArn?: string;
    /**
     * The domain name.
     */
    readonly domainId?: string;
    readonly domainSettings?: outputs.sagemaker.DomainSettings;
    /**
     * The ID of the Amazon Elastic File System (EFS) managed by this Domain.
     */
    readonly homeEfsFileSystemId?: string;
    /**
     * The ID of the security group that authorizes traffic between the RSessionGateway apps and the RStudioServerPro app.
     */
    readonly securityGroupIdForDomainBoundary?: string;
    /**
     * The ARN of the application managed by SageMaker in IAM Identity Center. This value is only returned for domains created after October 1, 2023.
     */
    readonly singleSignOnApplicationArn?: string;
    /**
     * The SSO managed application instance ID.
     */
    readonly singleSignOnManagedApplicationInstanceId?: string;
    /**
     * The VPC subnets that Studio uses for communication.
     */
    readonly subnetIds?: string[];
    /**
     * The URL to the created domain.
     */
    readonly url?: string;
}
/**
 * Resource Type definition for AWS::SageMaker::Domain
 */
export function getDomainOutput(args: GetDomainOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDomainResult> {
    return pulumi.output(args).apply((a: any) => getDomain(a, opts))
}

export interface GetDomainOutputArgs {
    /**
     * The domain name.
     */
    domainId: pulumi.Input<string>;
}
