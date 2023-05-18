// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Transfer::Agreement
 */
export function getAgreement(args: GetAgreementArgs, opts?: pulumi.InvokeOptions): Promise<GetAgreementResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:transfer:getAgreement", {
        "agreementId": args.agreementId,
        "serverId": args.serverId,
    }, opts);
}

export interface GetAgreementArgs {
    /**
     * A unique identifier for the agreement.
     */
    agreementId: string;
    /**
     * A unique identifier for the server.
     */
    serverId: string;
}

export interface GetAgreementResult {
    /**
     * Specifies the access role for the agreement.
     */
    readonly accessRole?: string;
    /**
     * A unique identifier for the agreement.
     */
    readonly agreementId?: string;
    /**
     * Specifies the unique Amazon Resource Name (ARN) for the agreement.
     */
    readonly arn?: string;
    /**
     * Specifies the base directory for the agreement.
     */
    readonly baseDirectory?: string;
    /**
     * A textual description for the agreement.
     */
    readonly description?: string;
    /**
     * A unique identifier for the local profile.
     */
    readonly localProfileId?: string;
    /**
     * A unique identifier for the partner profile.
     */
    readonly partnerProfileId?: string;
    /**
     * Specifies the status of the agreement.
     */
    readonly status?: enums.transfer.AgreementStatus;
    /**
     * Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.
     */
    readonly tags?: outputs.transfer.AgreementTag[];
}
/**
 * Resource Type definition for AWS::Transfer::Agreement
 */
export function getAgreementOutput(args: GetAgreementOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAgreementResult> {
    return pulumi.output(args).apply((a: any) => getAgreement(a, opts))
}

export interface GetAgreementOutputArgs {
    /**
     * A unique identifier for the agreement.
     */
    agreementId: pulumi.Input<string>;
    /**
     * A unique identifier for the server.
     */
    serverId: pulumi.Input<string>;
}
