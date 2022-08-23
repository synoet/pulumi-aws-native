// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SES::EmailIdentity
 */
export class EmailIdentity extends pulumi.CustomResource {
    /**
     * Get an existing EmailIdentity resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): EmailIdentity {
        return new EmailIdentity(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ses:EmailIdentity';

    /**
     * Returns true if the given object is an instance of EmailIdentity.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EmailIdentity {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EmailIdentity.__pulumiType;
    }

    public readonly configurationSetAttributes!: pulumi.Output<outputs.ses.EmailIdentityConfigurationSetAttributes | undefined>;
    public readonly dkimAttributes!: pulumi.Output<outputs.ses.EmailIdentityDkimAttributes | undefined>;
    public /*out*/ readonly dkimDNSTokenName1!: pulumi.Output<string>;
    public /*out*/ readonly dkimDNSTokenName2!: pulumi.Output<string>;
    public /*out*/ readonly dkimDNSTokenName3!: pulumi.Output<string>;
    public /*out*/ readonly dkimDNSTokenValue1!: pulumi.Output<string>;
    public /*out*/ readonly dkimDNSTokenValue2!: pulumi.Output<string>;
    public /*out*/ readonly dkimDNSTokenValue3!: pulumi.Output<string>;
    public readonly dkimSigningAttributes!: pulumi.Output<outputs.ses.EmailIdentityDkimSigningAttributes | undefined>;
    /**
     * The email address or domain to verify.
     */
    public readonly emailIdentity!: pulumi.Output<string>;
    public readonly feedbackAttributes!: pulumi.Output<outputs.ses.EmailIdentityFeedbackAttributes | undefined>;
    public readonly mailFromAttributes!: pulumi.Output<outputs.ses.EmailIdentityMailFromAttributes | undefined>;

    /**
     * Create a EmailIdentity resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: EmailIdentityArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.emailIdentity === undefined) && !opts.urn) {
                throw new Error("Missing required property 'emailIdentity'");
            }
            resourceInputs["configurationSetAttributes"] = args ? args.configurationSetAttributes : undefined;
            resourceInputs["dkimAttributes"] = args ? args.dkimAttributes : undefined;
            resourceInputs["dkimSigningAttributes"] = args ? args.dkimSigningAttributes : undefined;
            resourceInputs["emailIdentity"] = args ? args.emailIdentity : undefined;
            resourceInputs["feedbackAttributes"] = args ? args.feedbackAttributes : undefined;
            resourceInputs["mailFromAttributes"] = args ? args.mailFromAttributes : undefined;
            resourceInputs["dkimDNSTokenName1"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenName2"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenName3"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenValue1"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenValue2"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenValue3"] = undefined /*out*/;
        } else {
            resourceInputs["configurationSetAttributes"] = undefined /*out*/;
            resourceInputs["dkimAttributes"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenName1"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenName2"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenName3"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenValue1"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenValue2"] = undefined /*out*/;
            resourceInputs["dkimDNSTokenValue3"] = undefined /*out*/;
            resourceInputs["dkimSigningAttributes"] = undefined /*out*/;
            resourceInputs["emailIdentity"] = undefined /*out*/;
            resourceInputs["feedbackAttributes"] = undefined /*out*/;
            resourceInputs["mailFromAttributes"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(EmailIdentity.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a EmailIdentity resource.
 */
export interface EmailIdentityArgs {
    configurationSetAttributes?: pulumi.Input<inputs.ses.EmailIdentityConfigurationSetAttributesArgs>;
    dkimAttributes?: pulumi.Input<inputs.ses.EmailIdentityDkimAttributesArgs>;
    dkimSigningAttributes?: pulumi.Input<inputs.ses.EmailIdentityDkimSigningAttributesArgs>;
    /**
     * The email address or domain to verify.
     */
    emailIdentity: pulumi.Input<string>;
    feedbackAttributes?: pulumi.Input<inputs.ses.EmailIdentityFeedbackAttributesArgs>;
    mailFromAttributes?: pulumi.Input<inputs.ses.EmailIdentityMailFromAttributesArgs>;
}
