// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package pcaconnectorad

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

var _ = internal.GetEnvOrDefault

type ConnectorTags struct {
}

// ConnectorTagsInput is an input type that accepts ConnectorTagsArgs and ConnectorTagsOutput values.
// You can construct a concrete instance of `ConnectorTagsInput` via:
//
//	ConnectorTagsArgs{...}
type ConnectorTagsInput interface {
	pulumi.Input

	ToConnectorTagsOutput() ConnectorTagsOutput
	ToConnectorTagsOutputWithContext(context.Context) ConnectorTagsOutput
}

type ConnectorTagsArgs struct {
}

func (ConnectorTagsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorTags)(nil)).Elem()
}

func (i ConnectorTagsArgs) ToConnectorTagsOutput() ConnectorTagsOutput {
	return i.ToConnectorTagsOutputWithContext(context.Background())
}

func (i ConnectorTagsArgs) ToConnectorTagsOutputWithContext(ctx context.Context) ConnectorTagsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorTagsOutput)
}

func (i ConnectorTagsArgs) ToOutput(ctx context.Context) pulumix.Output[ConnectorTags] {
	return pulumix.Output[ConnectorTags]{
		OutputState: i.ToConnectorTagsOutputWithContext(ctx).OutputState,
	}
}

func (i ConnectorTagsArgs) ToConnectorTagsPtrOutput() ConnectorTagsPtrOutput {
	return i.ToConnectorTagsPtrOutputWithContext(context.Background())
}

func (i ConnectorTagsArgs) ToConnectorTagsPtrOutputWithContext(ctx context.Context) ConnectorTagsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorTagsOutput).ToConnectorTagsPtrOutputWithContext(ctx)
}

// ConnectorTagsPtrInput is an input type that accepts ConnectorTagsArgs, ConnectorTagsPtr and ConnectorTagsPtrOutput values.
// You can construct a concrete instance of `ConnectorTagsPtrInput` via:
//
//	        ConnectorTagsArgs{...}
//
//	or:
//
//	        nil
type ConnectorTagsPtrInput interface {
	pulumi.Input

	ToConnectorTagsPtrOutput() ConnectorTagsPtrOutput
	ToConnectorTagsPtrOutputWithContext(context.Context) ConnectorTagsPtrOutput
}

type connectorTagsPtrType ConnectorTagsArgs

func ConnectorTagsPtr(v *ConnectorTagsArgs) ConnectorTagsPtrInput {
	return (*connectorTagsPtrType)(v)
}

func (*connectorTagsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectorTags)(nil)).Elem()
}

func (i *connectorTagsPtrType) ToConnectorTagsPtrOutput() ConnectorTagsPtrOutput {
	return i.ToConnectorTagsPtrOutputWithContext(context.Background())
}

func (i *connectorTagsPtrType) ToConnectorTagsPtrOutputWithContext(ctx context.Context) ConnectorTagsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorTagsPtrOutput)
}

func (i *connectorTagsPtrType) ToOutput(ctx context.Context) pulumix.Output[*ConnectorTags] {
	return pulumix.Output[*ConnectorTags]{
		OutputState: i.ToConnectorTagsPtrOutputWithContext(ctx).OutputState,
	}
}

type ConnectorTagsOutput struct{ *pulumi.OutputState }

func (ConnectorTagsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorTags)(nil)).Elem()
}

func (o ConnectorTagsOutput) ToConnectorTagsOutput() ConnectorTagsOutput {
	return o
}

func (o ConnectorTagsOutput) ToConnectorTagsOutputWithContext(ctx context.Context) ConnectorTagsOutput {
	return o
}

func (o ConnectorTagsOutput) ToConnectorTagsPtrOutput() ConnectorTagsPtrOutput {
	return o.ToConnectorTagsPtrOutputWithContext(context.Background())
}

func (o ConnectorTagsOutput) ToConnectorTagsPtrOutputWithContext(ctx context.Context) ConnectorTagsPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ConnectorTags) *ConnectorTags {
		return &v
	}).(ConnectorTagsPtrOutput)
}

func (o ConnectorTagsOutput) ToOutput(ctx context.Context) pulumix.Output[ConnectorTags] {
	return pulumix.Output[ConnectorTags]{
		OutputState: o.OutputState,
	}
}

type ConnectorTagsPtrOutput struct{ *pulumi.OutputState }

func (ConnectorTagsPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectorTags)(nil)).Elem()
}

func (o ConnectorTagsPtrOutput) ToConnectorTagsPtrOutput() ConnectorTagsPtrOutput {
	return o
}

func (o ConnectorTagsPtrOutput) ToConnectorTagsPtrOutputWithContext(ctx context.Context) ConnectorTagsPtrOutput {
	return o
}

func (o ConnectorTagsPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ConnectorTags] {
	return pulumix.Output[*ConnectorTags]{
		OutputState: o.OutputState,
	}
}

func (o ConnectorTagsPtrOutput) Elem() ConnectorTagsOutput {
	return o.ApplyT(func(v *ConnectorTags) ConnectorTags {
		if v != nil {
			return *v
		}
		var ret ConnectorTags
		return ret
	}).(ConnectorTagsOutput)
}

type ConnectorVpcInformation struct {
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
}

// ConnectorVpcInformationInput is an input type that accepts ConnectorVpcInformationArgs and ConnectorVpcInformationOutput values.
// You can construct a concrete instance of `ConnectorVpcInformationInput` via:
//
//	ConnectorVpcInformationArgs{...}
type ConnectorVpcInformationInput interface {
	pulumi.Input

	ToConnectorVpcInformationOutput() ConnectorVpcInformationOutput
	ToConnectorVpcInformationOutputWithContext(context.Context) ConnectorVpcInformationOutput
}

type ConnectorVpcInformationArgs struct {
	SecurityGroupIds pulumi.StringArrayInput `pulumi:"securityGroupIds"`
}

func (ConnectorVpcInformationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorVpcInformation)(nil)).Elem()
}

func (i ConnectorVpcInformationArgs) ToConnectorVpcInformationOutput() ConnectorVpcInformationOutput {
	return i.ToConnectorVpcInformationOutputWithContext(context.Background())
}

func (i ConnectorVpcInformationArgs) ToConnectorVpcInformationOutputWithContext(ctx context.Context) ConnectorVpcInformationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorVpcInformationOutput)
}

func (i ConnectorVpcInformationArgs) ToOutput(ctx context.Context) pulumix.Output[ConnectorVpcInformation] {
	return pulumix.Output[ConnectorVpcInformation]{
		OutputState: i.ToConnectorVpcInformationOutputWithContext(ctx).OutputState,
	}
}

type ConnectorVpcInformationOutput struct{ *pulumi.OutputState }

func (ConnectorVpcInformationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorVpcInformation)(nil)).Elem()
}

func (o ConnectorVpcInformationOutput) ToConnectorVpcInformationOutput() ConnectorVpcInformationOutput {
	return o
}

func (o ConnectorVpcInformationOutput) ToConnectorVpcInformationOutputWithContext(ctx context.Context) ConnectorVpcInformationOutput {
	return o
}

func (o ConnectorVpcInformationOutput) ToOutput(ctx context.Context) pulumix.Output[ConnectorVpcInformation] {
	return pulumix.Output[ConnectorVpcInformation]{
		OutputState: o.OutputState,
	}
}

func (o ConnectorVpcInformationOutput) SecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ConnectorVpcInformation) []string { return v.SecurityGroupIds }).(pulumi.StringArrayOutput)
}

type DirectoryRegistrationTags struct {
}

// DirectoryRegistrationTagsInput is an input type that accepts DirectoryRegistrationTagsArgs and DirectoryRegistrationTagsOutput values.
// You can construct a concrete instance of `DirectoryRegistrationTagsInput` via:
//
//	DirectoryRegistrationTagsArgs{...}
type DirectoryRegistrationTagsInput interface {
	pulumi.Input

	ToDirectoryRegistrationTagsOutput() DirectoryRegistrationTagsOutput
	ToDirectoryRegistrationTagsOutputWithContext(context.Context) DirectoryRegistrationTagsOutput
}

type DirectoryRegistrationTagsArgs struct {
}

func (DirectoryRegistrationTagsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DirectoryRegistrationTags)(nil)).Elem()
}

func (i DirectoryRegistrationTagsArgs) ToDirectoryRegistrationTagsOutput() DirectoryRegistrationTagsOutput {
	return i.ToDirectoryRegistrationTagsOutputWithContext(context.Background())
}

func (i DirectoryRegistrationTagsArgs) ToDirectoryRegistrationTagsOutputWithContext(ctx context.Context) DirectoryRegistrationTagsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DirectoryRegistrationTagsOutput)
}

func (i DirectoryRegistrationTagsArgs) ToOutput(ctx context.Context) pulumix.Output[DirectoryRegistrationTags] {
	return pulumix.Output[DirectoryRegistrationTags]{
		OutputState: i.ToDirectoryRegistrationTagsOutputWithContext(ctx).OutputState,
	}
}

func (i DirectoryRegistrationTagsArgs) ToDirectoryRegistrationTagsPtrOutput() DirectoryRegistrationTagsPtrOutput {
	return i.ToDirectoryRegistrationTagsPtrOutputWithContext(context.Background())
}

func (i DirectoryRegistrationTagsArgs) ToDirectoryRegistrationTagsPtrOutputWithContext(ctx context.Context) DirectoryRegistrationTagsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DirectoryRegistrationTagsOutput).ToDirectoryRegistrationTagsPtrOutputWithContext(ctx)
}

// DirectoryRegistrationTagsPtrInput is an input type that accepts DirectoryRegistrationTagsArgs, DirectoryRegistrationTagsPtr and DirectoryRegistrationTagsPtrOutput values.
// You can construct a concrete instance of `DirectoryRegistrationTagsPtrInput` via:
//
//	        DirectoryRegistrationTagsArgs{...}
//
//	or:
//
//	        nil
type DirectoryRegistrationTagsPtrInput interface {
	pulumi.Input

	ToDirectoryRegistrationTagsPtrOutput() DirectoryRegistrationTagsPtrOutput
	ToDirectoryRegistrationTagsPtrOutputWithContext(context.Context) DirectoryRegistrationTagsPtrOutput
}

type directoryRegistrationTagsPtrType DirectoryRegistrationTagsArgs

func DirectoryRegistrationTagsPtr(v *DirectoryRegistrationTagsArgs) DirectoryRegistrationTagsPtrInput {
	return (*directoryRegistrationTagsPtrType)(v)
}

func (*directoryRegistrationTagsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**DirectoryRegistrationTags)(nil)).Elem()
}

func (i *directoryRegistrationTagsPtrType) ToDirectoryRegistrationTagsPtrOutput() DirectoryRegistrationTagsPtrOutput {
	return i.ToDirectoryRegistrationTagsPtrOutputWithContext(context.Background())
}

func (i *directoryRegistrationTagsPtrType) ToDirectoryRegistrationTagsPtrOutputWithContext(ctx context.Context) DirectoryRegistrationTagsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DirectoryRegistrationTagsPtrOutput)
}

func (i *directoryRegistrationTagsPtrType) ToOutput(ctx context.Context) pulumix.Output[*DirectoryRegistrationTags] {
	return pulumix.Output[*DirectoryRegistrationTags]{
		OutputState: i.ToDirectoryRegistrationTagsPtrOutputWithContext(ctx).OutputState,
	}
}

type DirectoryRegistrationTagsOutput struct{ *pulumi.OutputState }

func (DirectoryRegistrationTagsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DirectoryRegistrationTags)(nil)).Elem()
}

func (o DirectoryRegistrationTagsOutput) ToDirectoryRegistrationTagsOutput() DirectoryRegistrationTagsOutput {
	return o
}

func (o DirectoryRegistrationTagsOutput) ToDirectoryRegistrationTagsOutputWithContext(ctx context.Context) DirectoryRegistrationTagsOutput {
	return o
}

func (o DirectoryRegistrationTagsOutput) ToDirectoryRegistrationTagsPtrOutput() DirectoryRegistrationTagsPtrOutput {
	return o.ToDirectoryRegistrationTagsPtrOutputWithContext(context.Background())
}

func (o DirectoryRegistrationTagsOutput) ToDirectoryRegistrationTagsPtrOutputWithContext(ctx context.Context) DirectoryRegistrationTagsPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DirectoryRegistrationTags) *DirectoryRegistrationTags {
		return &v
	}).(DirectoryRegistrationTagsPtrOutput)
}

func (o DirectoryRegistrationTagsOutput) ToOutput(ctx context.Context) pulumix.Output[DirectoryRegistrationTags] {
	return pulumix.Output[DirectoryRegistrationTags]{
		OutputState: o.OutputState,
	}
}

type DirectoryRegistrationTagsPtrOutput struct{ *pulumi.OutputState }

func (DirectoryRegistrationTagsPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DirectoryRegistrationTags)(nil)).Elem()
}

func (o DirectoryRegistrationTagsPtrOutput) ToDirectoryRegistrationTagsPtrOutput() DirectoryRegistrationTagsPtrOutput {
	return o
}

func (o DirectoryRegistrationTagsPtrOutput) ToDirectoryRegistrationTagsPtrOutputWithContext(ctx context.Context) DirectoryRegistrationTagsPtrOutput {
	return o
}

func (o DirectoryRegistrationTagsPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*DirectoryRegistrationTags] {
	return pulumix.Output[*DirectoryRegistrationTags]{
		OutputState: o.OutputState,
	}
}

func (o DirectoryRegistrationTagsPtrOutput) Elem() DirectoryRegistrationTagsOutput {
	return o.ApplyT(func(v *DirectoryRegistrationTags) DirectoryRegistrationTags {
		if v != nil {
			return *v
		}
		var ret DirectoryRegistrationTags
		return ret
	}).(DirectoryRegistrationTagsOutput)
}

type TemplateApplicationPolicies struct {
	Critical *bool         `pulumi:"critical"`
	Policies []interface{} `pulumi:"policies"`
}

type TemplateApplicationPolicy0Properties struct {
	PolicyType TemplateApplicationPolicyType `pulumi:"policyType"`
}

type TemplateApplicationPolicy1Properties struct {
	PolicyObjectIdentifier string `pulumi:"policyObjectIdentifier"`
}

type TemplateCertificateValidity struct {
	RenewalPeriod  TemplateValidityPeriod `pulumi:"renewalPeriod"`
	ValidityPeriod TemplateValidityPeriod `pulumi:"validityPeriod"`
}

type TemplateDefinition0Properties struct {
	TemplateV2 TemplateV2 `pulumi:"templateV2"`
}

type TemplateDefinition1Properties struct {
	TemplateV3 TemplateV3 `pulumi:"templateV3"`
}

type TemplateDefinition2Properties struct {
	TemplateV4 TemplateV4 `pulumi:"templateV4"`
}

type TemplateEnrollmentFlagsV2 struct {
	EnableKeyReuseOnNtTokenKeysetStorageFull  *bool `pulumi:"enableKeyReuseOnNtTokenKeysetStorageFull"`
	IncludeSymmetricAlgorithms                *bool `pulumi:"includeSymmetricAlgorithms"`
	NoSecurityExtension                       *bool `pulumi:"noSecurityExtension"`
	RemoveInvalidCertificateFromPersonalStore *bool `pulumi:"removeInvalidCertificateFromPersonalStore"`
	UserInteractionRequired                   *bool `pulumi:"userInteractionRequired"`
}

type TemplateEnrollmentFlagsV3 struct {
	EnableKeyReuseOnNtTokenKeysetStorageFull  *bool `pulumi:"enableKeyReuseOnNtTokenKeysetStorageFull"`
	IncludeSymmetricAlgorithms                *bool `pulumi:"includeSymmetricAlgorithms"`
	NoSecurityExtension                       *bool `pulumi:"noSecurityExtension"`
	RemoveInvalidCertificateFromPersonalStore *bool `pulumi:"removeInvalidCertificateFromPersonalStore"`
	UserInteractionRequired                   *bool `pulumi:"userInteractionRequired"`
}

type TemplateEnrollmentFlagsV4 struct {
	EnableKeyReuseOnNtTokenKeysetStorageFull  *bool `pulumi:"enableKeyReuseOnNtTokenKeysetStorageFull"`
	IncludeSymmetricAlgorithms                *bool `pulumi:"includeSymmetricAlgorithms"`
	NoSecurityExtension                       *bool `pulumi:"noSecurityExtension"`
	RemoveInvalidCertificateFromPersonalStore *bool `pulumi:"removeInvalidCertificateFromPersonalStore"`
	UserInteractionRequired                   *bool `pulumi:"userInteractionRequired"`
}

type TemplateExtensionsV2 struct {
	ApplicationPolicies *TemplateApplicationPolicies `pulumi:"applicationPolicies"`
	KeyUsage            TemplateKeyUsage             `pulumi:"keyUsage"`
}

type TemplateExtensionsV3 struct {
	ApplicationPolicies *TemplateApplicationPolicies `pulumi:"applicationPolicies"`
	KeyUsage            TemplateKeyUsage             `pulumi:"keyUsage"`
}

type TemplateExtensionsV4 struct {
	ApplicationPolicies *TemplateApplicationPolicies `pulumi:"applicationPolicies"`
	KeyUsage            TemplateKeyUsage             `pulumi:"keyUsage"`
}

type TemplateGeneralFlagsV2 struct {
	AutoEnrollment *bool `pulumi:"autoEnrollment"`
	MachineType    *bool `pulumi:"machineType"`
}

type TemplateGeneralFlagsV3 struct {
	AutoEnrollment *bool `pulumi:"autoEnrollment"`
	MachineType    *bool `pulumi:"machineType"`
}

type TemplateGeneralFlagsV4 struct {
	AutoEnrollment *bool `pulumi:"autoEnrollment"`
	MachineType    *bool `pulumi:"machineType"`
}

type TemplateGroupAccessControlEntryAccessRights struct {
	AutoEnroll *TemplateGroupAccessControlEntryAccessRight `pulumi:"autoEnroll"`
	Enroll     *TemplateGroupAccessControlEntryAccessRight `pulumi:"enroll"`
}

// TemplateGroupAccessControlEntryAccessRightsInput is an input type that accepts TemplateGroupAccessControlEntryAccessRightsArgs and TemplateGroupAccessControlEntryAccessRightsOutput values.
// You can construct a concrete instance of `TemplateGroupAccessControlEntryAccessRightsInput` via:
//
//	TemplateGroupAccessControlEntryAccessRightsArgs{...}
type TemplateGroupAccessControlEntryAccessRightsInput interface {
	pulumi.Input

	ToTemplateGroupAccessControlEntryAccessRightsOutput() TemplateGroupAccessControlEntryAccessRightsOutput
	ToTemplateGroupAccessControlEntryAccessRightsOutputWithContext(context.Context) TemplateGroupAccessControlEntryAccessRightsOutput
}

type TemplateGroupAccessControlEntryAccessRightsArgs struct {
	AutoEnroll TemplateGroupAccessControlEntryAccessRightPtrInput `pulumi:"autoEnroll"`
	Enroll     TemplateGroupAccessControlEntryAccessRightPtrInput `pulumi:"enroll"`
}

func (TemplateGroupAccessControlEntryAccessRightsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TemplateGroupAccessControlEntryAccessRights)(nil)).Elem()
}

func (i TemplateGroupAccessControlEntryAccessRightsArgs) ToTemplateGroupAccessControlEntryAccessRightsOutput() TemplateGroupAccessControlEntryAccessRightsOutput {
	return i.ToTemplateGroupAccessControlEntryAccessRightsOutputWithContext(context.Background())
}

func (i TemplateGroupAccessControlEntryAccessRightsArgs) ToTemplateGroupAccessControlEntryAccessRightsOutputWithContext(ctx context.Context) TemplateGroupAccessControlEntryAccessRightsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TemplateGroupAccessControlEntryAccessRightsOutput)
}

func (i TemplateGroupAccessControlEntryAccessRightsArgs) ToOutput(ctx context.Context) pulumix.Output[TemplateGroupAccessControlEntryAccessRights] {
	return pulumix.Output[TemplateGroupAccessControlEntryAccessRights]{
		OutputState: i.ToTemplateGroupAccessControlEntryAccessRightsOutputWithContext(ctx).OutputState,
	}
}

type TemplateGroupAccessControlEntryAccessRightsOutput struct{ *pulumi.OutputState }

func (TemplateGroupAccessControlEntryAccessRightsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TemplateGroupAccessControlEntryAccessRights)(nil)).Elem()
}

func (o TemplateGroupAccessControlEntryAccessRightsOutput) ToTemplateGroupAccessControlEntryAccessRightsOutput() TemplateGroupAccessControlEntryAccessRightsOutput {
	return o
}

func (o TemplateGroupAccessControlEntryAccessRightsOutput) ToTemplateGroupAccessControlEntryAccessRightsOutputWithContext(ctx context.Context) TemplateGroupAccessControlEntryAccessRightsOutput {
	return o
}

func (o TemplateGroupAccessControlEntryAccessRightsOutput) ToOutput(ctx context.Context) pulumix.Output[TemplateGroupAccessControlEntryAccessRights] {
	return pulumix.Output[TemplateGroupAccessControlEntryAccessRights]{
		OutputState: o.OutputState,
	}
}

func (o TemplateGroupAccessControlEntryAccessRightsOutput) AutoEnroll() TemplateGroupAccessControlEntryAccessRightPtrOutput {
	return o.ApplyT(func(v TemplateGroupAccessControlEntryAccessRights) *TemplateGroupAccessControlEntryAccessRight {
		return v.AutoEnroll
	}).(TemplateGroupAccessControlEntryAccessRightPtrOutput)
}

func (o TemplateGroupAccessControlEntryAccessRightsOutput) Enroll() TemplateGroupAccessControlEntryAccessRightPtrOutput {
	return o.ApplyT(func(v TemplateGroupAccessControlEntryAccessRights) *TemplateGroupAccessControlEntryAccessRight {
		return v.Enroll
	}).(TemplateGroupAccessControlEntryAccessRightPtrOutput)
}

type TemplateKeyUsage struct {
	Critical   *bool                 `pulumi:"critical"`
	UsageFlags TemplateKeyUsageFlags `pulumi:"usageFlags"`
}

type TemplateKeyUsageFlags struct {
	DataEncipherment *bool `pulumi:"dataEncipherment"`
	DigitalSignature *bool `pulumi:"digitalSignature"`
	KeyAgreement     *bool `pulumi:"keyAgreement"`
	KeyEncipherment  *bool `pulumi:"keyEncipherment"`
	NonRepudiation   *bool `pulumi:"nonRepudiation"`
}

type TemplateKeyUsageProperty0Properties struct {
	PropertyType TemplateKeyUsagePropertyType `pulumi:"propertyType"`
}

type TemplateKeyUsageProperty1Properties struct {
	PropertyFlags TemplateKeyUsagePropertyFlags `pulumi:"propertyFlags"`
}

type TemplateKeyUsagePropertyFlags struct {
	Decrypt      *bool `pulumi:"decrypt"`
	KeyAgreement *bool `pulumi:"keyAgreement"`
	Sign         *bool `pulumi:"sign"`
}

type TemplatePrivateKeyAttributesV2 struct {
	CryptoProviders  []string        `pulumi:"cryptoProviders"`
	KeySpec          TemplateKeySpec `pulumi:"keySpec"`
	MinimalKeyLength float64         `pulumi:"minimalKeyLength"`
}

type TemplatePrivateKeyAttributesV3 struct {
	Algorithm        TemplatePrivateKeyAlgorithm `pulumi:"algorithm"`
	CryptoProviders  []string                    `pulumi:"cryptoProviders"`
	KeySpec          TemplateKeySpec             `pulumi:"keySpec"`
	KeyUsageProperty interface{}                 `pulumi:"keyUsageProperty"`
	MinimalKeyLength float64                     `pulumi:"minimalKeyLength"`
}

type TemplatePrivateKeyAttributesV4 struct {
	Algorithm        *TemplatePrivateKeyAlgorithm `pulumi:"algorithm"`
	CryptoProviders  []string                     `pulumi:"cryptoProviders"`
	KeySpec          TemplateKeySpec              `pulumi:"keySpec"`
	KeyUsageProperty interface{}                  `pulumi:"keyUsageProperty"`
	MinimalKeyLength float64                      `pulumi:"minimalKeyLength"`
}

type TemplatePrivateKeyFlagsV2 struct {
	ClientVersion               TemplateClientCompatibilityV2 `pulumi:"clientVersion"`
	ExportableKey               *bool                         `pulumi:"exportableKey"`
	StrongKeyProtectionRequired *bool                         `pulumi:"strongKeyProtectionRequired"`
}

type TemplatePrivateKeyFlagsV3 struct {
	ClientVersion                      TemplateClientCompatibilityV3 `pulumi:"clientVersion"`
	ExportableKey                      *bool                         `pulumi:"exportableKey"`
	RequireAlternateSignatureAlgorithm *bool                         `pulumi:"requireAlternateSignatureAlgorithm"`
	StrongKeyProtectionRequired        *bool                         `pulumi:"strongKeyProtectionRequired"`
}

type TemplatePrivateKeyFlagsV4 struct {
	ClientVersion                      TemplateClientCompatibilityV4 `pulumi:"clientVersion"`
	ExportableKey                      *bool                         `pulumi:"exportableKey"`
	RequireAlternateSignatureAlgorithm *bool                         `pulumi:"requireAlternateSignatureAlgorithm"`
	RequireSameKeyRenewal              *bool                         `pulumi:"requireSameKeyRenewal"`
	StrongKeyProtectionRequired        *bool                         `pulumi:"strongKeyProtectionRequired"`
	UseLegacyProvider                  *bool                         `pulumi:"useLegacyProvider"`
}

type TemplateSubjectNameFlagsV2 struct {
	RequireCommonName       *bool `pulumi:"requireCommonName"`
	RequireDirectoryPath    *bool `pulumi:"requireDirectoryPath"`
	RequireDnsAsCn          *bool `pulumi:"requireDnsAsCn"`
	RequireEmail            *bool `pulumi:"requireEmail"`
	SanRequireDirectoryGuid *bool `pulumi:"sanRequireDirectoryGuid"`
	SanRequireDns           *bool `pulumi:"sanRequireDns"`
	SanRequireDomainDns     *bool `pulumi:"sanRequireDomainDns"`
	SanRequireEmail         *bool `pulumi:"sanRequireEmail"`
	SanRequireSpn           *bool `pulumi:"sanRequireSpn"`
	SanRequireUpn           *bool `pulumi:"sanRequireUpn"`
}

type TemplateSubjectNameFlagsV3 struct {
	RequireCommonName       *bool `pulumi:"requireCommonName"`
	RequireDirectoryPath    *bool `pulumi:"requireDirectoryPath"`
	RequireDnsAsCn          *bool `pulumi:"requireDnsAsCn"`
	RequireEmail            *bool `pulumi:"requireEmail"`
	SanRequireDirectoryGuid *bool `pulumi:"sanRequireDirectoryGuid"`
	SanRequireDns           *bool `pulumi:"sanRequireDns"`
	SanRequireDomainDns     *bool `pulumi:"sanRequireDomainDns"`
	SanRequireEmail         *bool `pulumi:"sanRequireEmail"`
	SanRequireSpn           *bool `pulumi:"sanRequireSpn"`
	SanRequireUpn           *bool `pulumi:"sanRequireUpn"`
}

type TemplateSubjectNameFlagsV4 struct {
	RequireCommonName       *bool `pulumi:"requireCommonName"`
	RequireDirectoryPath    *bool `pulumi:"requireDirectoryPath"`
	RequireDnsAsCn          *bool `pulumi:"requireDnsAsCn"`
	RequireEmail            *bool `pulumi:"requireEmail"`
	SanRequireDirectoryGuid *bool `pulumi:"sanRequireDirectoryGuid"`
	SanRequireDns           *bool `pulumi:"sanRequireDns"`
	SanRequireDomainDns     *bool `pulumi:"sanRequireDomainDns"`
	SanRequireEmail         *bool `pulumi:"sanRequireEmail"`
	SanRequireSpn           *bool `pulumi:"sanRequireSpn"`
	SanRequireUpn           *bool `pulumi:"sanRequireUpn"`
}

type TemplateTags struct {
}

// TemplateTagsInput is an input type that accepts TemplateTagsArgs and TemplateTagsOutput values.
// You can construct a concrete instance of `TemplateTagsInput` via:
//
//	TemplateTagsArgs{...}
type TemplateTagsInput interface {
	pulumi.Input

	ToTemplateTagsOutput() TemplateTagsOutput
	ToTemplateTagsOutputWithContext(context.Context) TemplateTagsOutput
}

type TemplateTagsArgs struct {
}

func (TemplateTagsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TemplateTags)(nil)).Elem()
}

func (i TemplateTagsArgs) ToTemplateTagsOutput() TemplateTagsOutput {
	return i.ToTemplateTagsOutputWithContext(context.Background())
}

func (i TemplateTagsArgs) ToTemplateTagsOutputWithContext(ctx context.Context) TemplateTagsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TemplateTagsOutput)
}

func (i TemplateTagsArgs) ToOutput(ctx context.Context) pulumix.Output[TemplateTags] {
	return pulumix.Output[TemplateTags]{
		OutputState: i.ToTemplateTagsOutputWithContext(ctx).OutputState,
	}
}

func (i TemplateTagsArgs) ToTemplateTagsPtrOutput() TemplateTagsPtrOutput {
	return i.ToTemplateTagsPtrOutputWithContext(context.Background())
}

func (i TemplateTagsArgs) ToTemplateTagsPtrOutputWithContext(ctx context.Context) TemplateTagsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TemplateTagsOutput).ToTemplateTagsPtrOutputWithContext(ctx)
}

// TemplateTagsPtrInput is an input type that accepts TemplateTagsArgs, TemplateTagsPtr and TemplateTagsPtrOutput values.
// You can construct a concrete instance of `TemplateTagsPtrInput` via:
//
//	        TemplateTagsArgs{...}
//
//	or:
//
//	        nil
type TemplateTagsPtrInput interface {
	pulumi.Input

	ToTemplateTagsPtrOutput() TemplateTagsPtrOutput
	ToTemplateTagsPtrOutputWithContext(context.Context) TemplateTagsPtrOutput
}

type templateTagsPtrType TemplateTagsArgs

func TemplateTagsPtr(v *TemplateTagsArgs) TemplateTagsPtrInput {
	return (*templateTagsPtrType)(v)
}

func (*templateTagsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**TemplateTags)(nil)).Elem()
}

func (i *templateTagsPtrType) ToTemplateTagsPtrOutput() TemplateTagsPtrOutput {
	return i.ToTemplateTagsPtrOutputWithContext(context.Background())
}

func (i *templateTagsPtrType) ToTemplateTagsPtrOutputWithContext(ctx context.Context) TemplateTagsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TemplateTagsPtrOutput)
}

func (i *templateTagsPtrType) ToOutput(ctx context.Context) pulumix.Output[*TemplateTags] {
	return pulumix.Output[*TemplateTags]{
		OutputState: i.ToTemplateTagsPtrOutputWithContext(ctx).OutputState,
	}
}

type TemplateTagsOutput struct{ *pulumi.OutputState }

func (TemplateTagsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TemplateTags)(nil)).Elem()
}

func (o TemplateTagsOutput) ToTemplateTagsOutput() TemplateTagsOutput {
	return o
}

func (o TemplateTagsOutput) ToTemplateTagsOutputWithContext(ctx context.Context) TemplateTagsOutput {
	return o
}

func (o TemplateTagsOutput) ToTemplateTagsPtrOutput() TemplateTagsPtrOutput {
	return o.ToTemplateTagsPtrOutputWithContext(context.Background())
}

func (o TemplateTagsOutput) ToTemplateTagsPtrOutputWithContext(ctx context.Context) TemplateTagsPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v TemplateTags) *TemplateTags {
		return &v
	}).(TemplateTagsPtrOutput)
}

func (o TemplateTagsOutput) ToOutput(ctx context.Context) pulumix.Output[TemplateTags] {
	return pulumix.Output[TemplateTags]{
		OutputState: o.OutputState,
	}
}

type TemplateTagsPtrOutput struct{ *pulumi.OutputState }

func (TemplateTagsPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TemplateTags)(nil)).Elem()
}

func (o TemplateTagsPtrOutput) ToTemplateTagsPtrOutput() TemplateTagsPtrOutput {
	return o
}

func (o TemplateTagsPtrOutput) ToTemplateTagsPtrOutputWithContext(ctx context.Context) TemplateTagsPtrOutput {
	return o
}

func (o TemplateTagsPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*TemplateTags] {
	return pulumix.Output[*TemplateTags]{
		OutputState: o.OutputState,
	}
}

func (o TemplateTagsPtrOutput) Elem() TemplateTagsOutput {
	return o.ApplyT(func(v *TemplateTags) TemplateTags {
		if v != nil {
			return *v
		}
		var ret TemplateTags
		return ret
	}).(TemplateTagsOutput)
}

type TemplateV2 struct {
	CertificateValidity  TemplateCertificateValidity    `pulumi:"certificateValidity"`
	EnrollmentFlags      TemplateEnrollmentFlagsV2      `pulumi:"enrollmentFlags"`
	Extensions           TemplateExtensionsV2           `pulumi:"extensions"`
	GeneralFlags         TemplateGeneralFlagsV2         `pulumi:"generalFlags"`
	PrivateKeyAttributes TemplatePrivateKeyAttributesV2 `pulumi:"privateKeyAttributes"`
	PrivateKeyFlags      TemplatePrivateKeyFlagsV2      `pulumi:"privateKeyFlags"`
	SubjectNameFlags     TemplateSubjectNameFlagsV2     `pulumi:"subjectNameFlags"`
	SupersededTemplates  []string                       `pulumi:"supersededTemplates"`
}

type TemplateV3 struct {
	CertificateValidity  TemplateCertificateValidity    `pulumi:"certificateValidity"`
	EnrollmentFlags      TemplateEnrollmentFlagsV3      `pulumi:"enrollmentFlags"`
	Extensions           TemplateExtensionsV3           `pulumi:"extensions"`
	GeneralFlags         TemplateGeneralFlagsV3         `pulumi:"generalFlags"`
	HashAlgorithm        TemplateHashAlgorithm          `pulumi:"hashAlgorithm"`
	PrivateKeyAttributes TemplatePrivateKeyAttributesV3 `pulumi:"privateKeyAttributes"`
	PrivateKeyFlags      TemplatePrivateKeyFlagsV3      `pulumi:"privateKeyFlags"`
	SubjectNameFlags     TemplateSubjectNameFlagsV3     `pulumi:"subjectNameFlags"`
	SupersededTemplates  []string                       `pulumi:"supersededTemplates"`
}

type TemplateV4 struct {
	CertificateValidity  TemplateCertificateValidity    `pulumi:"certificateValidity"`
	EnrollmentFlags      TemplateEnrollmentFlagsV4      `pulumi:"enrollmentFlags"`
	Extensions           TemplateExtensionsV4           `pulumi:"extensions"`
	GeneralFlags         TemplateGeneralFlagsV4         `pulumi:"generalFlags"`
	HashAlgorithm        *TemplateHashAlgorithm         `pulumi:"hashAlgorithm"`
	PrivateKeyAttributes TemplatePrivateKeyAttributesV4 `pulumi:"privateKeyAttributes"`
	PrivateKeyFlags      TemplatePrivateKeyFlagsV4      `pulumi:"privateKeyFlags"`
	SubjectNameFlags     TemplateSubjectNameFlagsV4     `pulumi:"subjectNameFlags"`
	SupersededTemplates  []string                       `pulumi:"supersededTemplates"`
}

type TemplateValidityPeriod struct {
	Period     float64                    `pulumi:"period"`
	PeriodType TemplateValidityPeriodType `pulumi:"periodType"`
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorTagsInput)(nil)).Elem(), ConnectorTagsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorTagsPtrInput)(nil)).Elem(), ConnectorTagsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorVpcInformationInput)(nil)).Elem(), ConnectorVpcInformationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DirectoryRegistrationTagsInput)(nil)).Elem(), DirectoryRegistrationTagsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DirectoryRegistrationTagsPtrInput)(nil)).Elem(), DirectoryRegistrationTagsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TemplateGroupAccessControlEntryAccessRightsInput)(nil)).Elem(), TemplateGroupAccessControlEntryAccessRightsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TemplateTagsInput)(nil)).Elem(), TemplateTagsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TemplateTagsPtrInput)(nil)).Elem(), TemplateTagsArgs{})
	pulumi.RegisterOutputType(ConnectorTagsOutput{})
	pulumi.RegisterOutputType(ConnectorTagsPtrOutput{})
	pulumi.RegisterOutputType(ConnectorVpcInformationOutput{})
	pulumi.RegisterOutputType(DirectoryRegistrationTagsOutput{})
	pulumi.RegisterOutputType(DirectoryRegistrationTagsPtrOutput{})
	pulumi.RegisterOutputType(TemplateGroupAccessControlEntryAccessRightsOutput{})
	pulumi.RegisterOutputType(TemplateTagsOutput{})
	pulumi.RegisterOutputType(TemplateTagsPtrOutput{})
}
