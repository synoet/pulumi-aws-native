// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Pinpoint::SmsTemplate
 *
 * @deprecated SmsTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class SmsTemplate extends pulumi.CustomResource {
    /**
     * Get an existing SmsTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SmsTemplate {
        pulumi.log.warn("SmsTemplate is deprecated: SmsTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new SmsTemplate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:pinpoint:SmsTemplate';

    /**
     * Returns true if the given object is an instance of SmsTemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SmsTemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SmsTemplate.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly body!: pulumi.Output<string>;
    public readonly defaultSubstitutions!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<any | undefined>;
    public readonly templateDescription!: pulumi.Output<string | undefined>;
    public readonly templateName!: pulumi.Output<string>;

    /**
     * Create a SmsTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated SmsTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: SmsTemplateArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("SmsTemplate is deprecated: SmsTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.body === undefined) && !opts.urn) {
                throw new Error("Missing required property 'body'");
            }
            if ((!args || args.templateName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'templateName'");
            }
            resourceInputs["body"] = args ? args.body : undefined;
            resourceInputs["defaultSubstitutions"] = args ? args.defaultSubstitutions : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["templateDescription"] = args ? args.templateDescription : undefined;
            resourceInputs["templateName"] = args ? args.templateName : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["body"] = undefined /*out*/;
            resourceInputs["defaultSubstitutions"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["templateDescription"] = undefined /*out*/;
            resourceInputs["templateName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["templateName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(SmsTemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SmsTemplate resource.
 */
export interface SmsTemplateArgs {
    body: pulumi.Input<string>;
    defaultSubstitutions?: pulumi.Input<string>;
    tags?: any;
    templateDescription?: pulumi.Input<string>;
    templateName: pulumi.Input<string>;
}
