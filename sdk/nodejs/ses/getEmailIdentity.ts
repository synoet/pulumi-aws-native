// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SES::EmailIdentity
 */
export function getEmailIdentity(args: GetEmailIdentityArgs, opts?: pulumi.InvokeOptions): Promise<GetEmailIdentityResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:ses:getEmailIdentity", {
        "emailIdentity": args.emailIdentity,
    }, opts);
}

export interface GetEmailIdentityArgs {
    /**
     * The email address or domain to verify.
     */
    emailIdentity: string;
}

export interface GetEmailIdentityResult {
    readonly configurationSetAttributes?: outputs.ses.EmailIdentityConfigurationSetAttributes;
    readonly dkimAttributes?: outputs.ses.EmailIdentityDkimAttributes;
    readonly dkimDNSTokenName1?: string;
    readonly dkimDNSTokenName2?: string;
    readonly dkimDNSTokenName3?: string;
    readonly dkimDNSTokenValue1?: string;
    readonly dkimDNSTokenValue2?: string;
    readonly dkimDNSTokenValue3?: string;
    readonly feedbackAttributes?: outputs.ses.EmailIdentityFeedbackAttributes;
    readonly mailFromAttributes?: outputs.ses.EmailIdentityMailFromAttributes;
}

export function getEmailIdentityOutput(args: GetEmailIdentityOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEmailIdentityResult> {
    return pulumi.output(args).apply(a => getEmailIdentity(a, opts))
}

export interface GetEmailIdentityOutputArgs {
    /**
     * The email address or domain to verify.
     */
    emailIdentity: pulumi.Input<string>;
}
