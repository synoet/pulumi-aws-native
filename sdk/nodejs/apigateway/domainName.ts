// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html
 */
export class DomainName extends pulumi.CustomResource {
    /**
     * Get an existing DomainName resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DomainName {
        return new DomainName(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigateway:DomainName';

    /**
     * Returns true if the given object is an instance of DomainName.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DomainName {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DomainName.__pulumiType;
    }

    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-certificatearn
     */
    public readonly certificateArn!: pulumi.Output<string | undefined>;
    public /*out*/ readonly distributionDomainName!: pulumi.Output<string>;
    public /*out*/ readonly distributionHostedZoneId!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-domainname
     */
    public readonly domainName!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-endpointconfiguration
     */
    public readonly endpointConfiguration!: pulumi.Output<outputs.apigateway.DomainNameEndpointConfiguration | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-mutualtlsauthentication
     */
    public readonly mutualTlsAuthentication!: pulumi.Output<outputs.apigateway.DomainNameMutualTlsAuthentication | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-ownershipverificationcertificatearn
     */
    public readonly ownershipVerificationCertificateArn!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-regionalcertificatearn
     */
    public readonly regionalCertificateArn!: pulumi.Output<string | undefined>;
    public /*out*/ readonly regionalDomainName!: pulumi.Output<string>;
    public /*out*/ readonly regionalHostedZoneId!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-securitypolicy
     */
    public readonly securityPolicy!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-tags
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a DomainName resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DomainNameArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["certificateArn"] = args ? args.certificateArn : undefined;
            inputs["domainName"] = args ? args.domainName : undefined;
            inputs["endpointConfiguration"] = args ? args.endpointConfiguration : undefined;
            inputs["mutualTlsAuthentication"] = args ? args.mutualTlsAuthentication : undefined;
            inputs["ownershipVerificationCertificateArn"] = args ? args.ownershipVerificationCertificateArn : undefined;
            inputs["regionalCertificateArn"] = args ? args.regionalCertificateArn : undefined;
            inputs["securityPolicy"] = args ? args.securityPolicy : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["distributionDomainName"] = undefined /*out*/;
            inputs["distributionHostedZoneId"] = undefined /*out*/;
            inputs["regionalDomainName"] = undefined /*out*/;
            inputs["regionalHostedZoneId"] = undefined /*out*/;
        } else {
            inputs["certificateArn"] = undefined /*out*/;
            inputs["distributionDomainName"] = undefined /*out*/;
            inputs["distributionHostedZoneId"] = undefined /*out*/;
            inputs["domainName"] = undefined /*out*/;
            inputs["endpointConfiguration"] = undefined /*out*/;
            inputs["mutualTlsAuthentication"] = undefined /*out*/;
            inputs["ownershipVerificationCertificateArn"] = undefined /*out*/;
            inputs["regionalCertificateArn"] = undefined /*out*/;
            inputs["regionalDomainName"] = undefined /*out*/;
            inputs["regionalHostedZoneId"] = undefined /*out*/;
            inputs["securityPolicy"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(DomainName.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a DomainName resource.
 */
export interface DomainNameArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-certificatearn
     */
    certificateArn?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-domainname
     */
    domainName?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-endpointconfiguration
     */
    endpointConfiguration?: pulumi.Input<inputs.apigateway.DomainNameEndpointConfigurationArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-mutualtlsauthentication
     */
    mutualTlsAuthentication?: pulumi.Input<inputs.apigateway.DomainNameMutualTlsAuthenticationArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-ownershipverificationcertificatearn
     */
    ownershipVerificationCertificateArn?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-regionalcertificatearn
     */
    regionalCertificateArn?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-securitypolicy
     */
    securityPolicy?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-tags
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
